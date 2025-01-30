import pandas as pd
import json
from openai import OpenAI

data = pd.read_csv('data_combined.csv')
#only columns conversation id, text and rubric
data = data[['conversation_id', 'text', 'rubric_4']]
#drop rows with missing values
data = data.dropna()

 # Filter rows where 'conversation_id' contains exactly two underscores
data_bridge = data[data['conversation_id'].str.contains(r'^[^_]*_[^_]*_[^_]*$', na=False)]

data_bridge1 = data_bridge[data_bridge['conversation_id'].str.endswith('1')]
data_bridge2 = data_bridge[data_bridge['conversation_id'].str.endswith('2')]

#all data not in bridge is in mathdial
data_mathdial = data[~data['conversation_id'].str.contains(r'^[^_]*_[^_]*_[^_]*$', na=False)]


# pick 5 rows randomly
val_set = data_bridge1.sample(5)
val_set = val_set.append(data_bridge2.sample(5))
val_set = val_set.append(data_mathdial.sample(10))

#rest 
rest_bridge1 = data_bridge1[~data_bridge1['conversation_id'].isin(val_set['conversation_id'])]
rest_bridge2 = data_bridge2[~data_bridge2['conversation_id'].isin(val_set['conversation_id'])]
rest_mathdial = data_mathdial[~data_mathdial['conversation_id'].isin(val_set['conversation_id'])]

train_set = rest_bridge1.sample(20)
train_set = train_set.append(rest_bridge2.sample(20))
train_set = train_set.append(rest_mathdial.sample(40))

test_set = data[~data['conversation_id'].isin(train_set['conversation_id'])&~data['conversation_id'].isin(val_set['conversation_id'])]

# Save the conversation_id for each set to separate text files
val_set['conversation_id'].to_csv('validation_set_ids.txt', index=False, header=False)
train_set['conversation_id'].to_csv('train_set_ids.txt', index=False, header=False)
test_set['conversation_id'].to_csv('test_set_ids.txt', index=False, header=False)





#{"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the capital of France?"}, {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}]}

#create batch file for training
with open('trainingfile.jsonl', 'w') as json_file:
    for index, row in train_set.iterrows():
        json.dump({"messages": [{"role": "system", "content": "You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor has a positive tone at their last utterance. Only answer Yes or No. "}, {"role": "user", "content": row['text']}, {"role": "assistant", "content": row['rubric_4']}]} , json_file)
        json_file.write('\n')

#create batch file for validation
with open('validationfile.jsonl', 'w') as json_file:
    for index, row in val_set.iterrows():
        json.dump({"messages": [{"role": "system", "content": "You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor has a positive tone at their last utterance. Only answer Yes or No. "}, {"role": "user", "content": row['text']}, {"role": "assistant", "content": row['rubric_4']}]} , json_file)
        json_file.write('\n')

client = OpenAI()

trainingfile = client.files.create(
  file=open("trainingfile.jsonl", "rb"),
  purpose="fine-tune"
)
validationfile = client.files.create(
  file=open("validationfile.jsonl", "rb"),
  purpose="fine-tune"
)
client.fine_tuning.jobs.create(
    training_file=trainingfile.id,
    validation_file=validationfile.id,
    model="gpt-4o-2024-08-06",  # or "gpt-4" for more advanced models
)