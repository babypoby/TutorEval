from transformers import (
    AutoTokenizer,
    DataCollatorWithPadding,
    TrainingArguments,
    Trainer,
    AutoModelForSequenceClassification,
)
from datasets import load_dataset, ClassLabel, Dataset
import numpy as np
import evaluate
import argparse
import os
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import torch


def compute_metrics(eval_pred):
    precision_metric = evaluate.load("precision")
    recall_metric = evaluate.load("recall")
    f1_metric = evaluate.load("f1")
    accuracy_metric = evaluate.load("accuracy")

    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)  
    precision = precision_metric.compute(
        predictions=preds, references=labels, average="binary"
    )["precision"]
    recall = recall_metric.compute(
        predictions=preds, references=labels, average="binary"
    )["recall"]
    f1 = f1_metric.compute(predictions=preds, references=labels, average="binary")["f1"]
    accuracy = accuracy_metric.compute(predictions=preds, references=labels)["accuracy"]

    report = classification_report(labels, preds)
    cm = confusion_matrix(labels, preds)
    print("Validation Report:\n" + report)
    print("Confusion Matrix:\n" + str(cm))

    return {
        "precision": precision,
        "recall": recall,
        "f1_binary": f1,
        "accuracy": accuracy,
    }


def main(args):
    df = pd.read_csv(args.dataset_path)

    # Convert the "response" column to binary labels: "Yes" = 1, "No" = 0
    df['response'] = df['response'].map({'Yes': 1, 'No': 0})

    dataset = Dataset.from_pandas(df)

    # Apply preprocessing and add labels to the tokenized data
    def preprocess(examples, tokenizer):
        tokenized = tokenizer(examples['text'], truncation=True, padding=True, max_length=512)
        tokenized['labels'] = examples['response']  # Add the labels here
        return tokenized

    # Define the model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.base_model_name)

    # Ensure padding token is available
    if not tokenizer.pad_token:
        tokenizer.pad_token = tokenizer.eos_token

    dataset = dataset.map(lambda examples: preprocess(examples, tokenizer), batched=True)

    # Cast 'response' to ClassLabel
    dataset = dataset.cast_column("response", ClassLabel(names=["No", "Yes"]))

    # Split the dataset into train and test (90%/10% split)
    dataset = dataset.train_test_split(test_size=0.1, stratify_by_column="response", seed=42)

    # Define the model
    model = AutoModelForSequenceClassification.from_pretrained(
        args.base_model_name,
        num_labels=2,  # Binary classification (0 or 1)
    )
    for name, param in model.named_parameters():
        if name.startswith("bert."):
            pass
            # param.requires_grad = False

    # Data collator for dynamic padding
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    training_args = TrainingArguments(
        output_dir=args.checkpoint_dir,
        hub_model_id=args.output_model_name,
        eval_strategy="steps",  # Evaluate every 'eval_steps' number of steps
        save_strategy="steps",  # Save the model every 'save_steps' number of steps
        eval_steps=1000,  # Evaluate every 1000 steps
        save_steps=1000,  # Save the model every 1000 steps
        logging_steps=100,
        learning_rate=3e-4,
        num_train_epochs=20,
        seed=0,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        eval_on_start=True,
        load_best_model_at_end=True,
        metric_for_best_model="eval_f1_binary",
        greater_is_better=True,
        # fp16=True,
        push_to_hub=True,
        gradient_accumulation_steps=2,
        # no_cuda=True,
    )
    if torch.backends.mps.is_available():
        print("Using MPS")

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"],
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics, 
    )

    trainer.train()
    trainer.save_model(os.path.join(args.checkpoint_dir, "final"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base_model_name", type=str, default="bert-base-uncased" 
    )
    parser.add_argument(
        "--dataset_path", type=str, default="bigdatachunk.csv"  # Path to CSV file
    )
    parser.add_argument(
        "--checkpoint_dir", type=str, default="./checkpoint_dir" 
    )
    parser.add_argument(
        "--output_model_name", type=str, default="babypoby/classify"
    )
    parser.add_argument("--use_mps_device", type=bool, default=True)
    args = parser.parse_args()
    main(args)
