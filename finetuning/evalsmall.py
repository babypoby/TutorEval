from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd

# Load the model and tokenizer from Hugging Face Hub
tokenizer = AutoTokenizer.from_pretrained("babypoby/classify")
model = AutoModelForSequenceClassification.from_pretrained("babypoby/classify")

# Example text input for classification
#text = "This is a sample text to classify. The tone seems positive."
data_r4 = pd.read_csv('data_combined.csv')
#only columns conversation id, text and rubric
data_r4 = data_r4[['conversation_id', 'text', 'rubric_4']]
#drop rows with missing values
data_r4 = data_r4.dropna()

test_set = pd.read_csv('test_set_ids.txt', header=None)
test_set.columns = ['conversation_id']

test = data_r4[data_r4['conversation_id'].isin(test_set['conversation_id'])]
test = test.rename(columns = {'rubric_4':'response'})

tp = 0
tn = 0
fp = 0
fn = 0

for (index,row) in test.iterrows():
    # Step 1: Tokenize the input text
    text = row['text']  
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Step 2: Perform inference
    outputs = model(**inputs)

    # Step 3: Interpret the logits
    logits = outputs.logits  # Raw scores from the model
    predicted_class = torch.argmax(logits, dim=-1).item()  # Convert to class index

    # Map predicted class to labels (if binary: 0 = "No", 1 = "Yes")
    label_map = {0: "No", 1: "Yes"}
    print(f"Predicted Class Index: {predicted_class}")
    print(f"Predicted Label: {label_map[predicted_class]}")

    print(f"Ground Truth Label: {row['response']}")

    # Step 4: Evaluate the model
    # Compare the predicted label with the ground truth label
    if label_map[predicted_class] == row['response']:
        if label_map[predicted_class] == "Yes":
            tp += 1
        else:
            tn += 1
    else:
        if label_map[predicted_class] == "Yes":
            fp += 1
        else:
            fn += 1

# Calculate the evaluation metrics
print(f"True Positives: {tp}")
print(f"True Negatives: {tn}")
print(f"False Positives: {fp}")
print(f"False Negatives: {fn}")




