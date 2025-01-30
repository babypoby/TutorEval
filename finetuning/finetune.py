from openai import OpenAI
import pandas as pd
import csv

# Initialize OpenAI client
client = OpenAI()

# Load the input CSV file
data = pd.read_csv('text_data_all.csv')

# Load ground truth data
data_r4 = pd.read_csv('data_combined.csv')
#only columns conversation id, text and rubric
data_r4 = data_r4[['conversation_id', 'text', 'rubric_4']]
#drop rows with missing values
data_r4 = data_r4.dropna()

#Data without ground truth, only predict conversations without ground truth
data = data[~data['conversation_id'].isin(data_r4['conversation_id'])]

print(len(data))

# Prepare a list to store responses
responses = []

# Open a CSV file to store responses (append mode)
with open('responses_new.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["conversation_id", "response"])
    writer.writeheader()  # Write headers once

    # Iterate over each row in the data
    for index, row in data.iterrows():
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
            responses.append(response_row)

            # Write to CSV file
            writer.writerow(response_row)

            print(f"Processed row {index} successfully!")
            print(response_text)

        except Exception as e:
            print(f"Error processing row {index}: {e}")
            continue

# Convert responses to DataFrame
responses_df = pd.DataFrame(responses)

# Merge the original data with responses
data = pd.merge(data, responses_df, on='conversation_id', how='left')

# Save the updated DataFrame back to a file
data.to_csv('text_data_all_with_responses_new.csv', index=False)

print("Responses saved and merged successfully!")


#save responses_df to csv



