from openai import OpenAI
import pandas as pd
import csv

# Initialize OpenAI client
client = OpenAI()
# Load ground truth data
data_r4 = pd.read_csv('data_combined.csv')
#only columns conversation id, text and rubric
data_r4 = data_r4[['conversation_id', 'text', 'rubric_4']]
#drop rows with missing values
data_r4 = data_r4.dropna()

test_set = pd.read_csv('test_set_ids.txt', header=None)
test_set.columns = ['conversation_id']

test = data_r4[data_r4['conversation_id'].isin(test_set['conversation_id'])]
test = test.rename(columns = {'rubric_4':'response'})
print(len(test))
print(test.head())
tp = 0
tn = 0
fp = 0
fn = 0

# Open a CSV file to store responses (append mode)
with open('test_responses.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["conversation_id", "response"])
    writer.writeheader()  # Write headers once

    # Iterate over each row in the data
    for index, row in test.iterrows():
        try:
            # Construct messages for API
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a Critic giving feedback on the Tutor's Tutoring skills. "
                        "For the given conversation, your task is to determine if the Tutor has a "
                        "positive tone at their last utterance. Only answer Yes or No."
                    )
                },
                {"role": "user", "content": row['text']}
            ]

            # Make the API call
            completion = client.chat.completions.create(
                model="ft:gpt-4o-2024-08-06:personal::Au55cf1W",
                messages=messages,
            )

            # Extract the response
            response_text = completion.choices[0].message.content

            # Save the response
            response_row = {"conversation_id": row['conversation_id'], "response": response_text}

            # Write to CSV file
            writer.writerow(response_row)

            print(f"Row {index}: {response_text} == {row['response']}")

            if response_text == row['response']:
                if response_text == "Yes":
                    tp += 1
                else:
                    tn += 1
            
            else:
                if response_text == "Yes":
                    fp += 1
                else:
                    fn += 1
                

        except Exception as e:
            print(f"Error processing row {index}: {e}")
            continue

print("True Positives: ", tp)
print("True Negatives: ", tn)
print("False Positives: ", fp)
print("False Negatives: ", fn)

# Convert responses to DataFrame
