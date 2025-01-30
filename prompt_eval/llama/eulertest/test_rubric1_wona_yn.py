import argparse
import ollama
import pandas as pd

# Set up argument parser
parser = argparse.ArgumentParser(description='Run Ollama model evaluation with a specified model.')
parser.add_argument('model_from', type=str, help='The model FROM parameter to use, e.g., "llama3:70b"')
args = parser.parse_args()

# Get the model FROM parameter from the command line argument
model_from = args.model_from

# Replace invalid characters for model naming
model_name_suffix = model_from.replace(':', '_').replace('/', '_')

data = pd.read_csv('data_combined.csv')


modelfile = f'''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor must never give away the correct solution. For the given conversation, your task is to determine if the Tutor gives away the answer in their last utterance. In every conversation, the student is currently incorrect. You can hence assume that the student made an error in the given conversation even though this is not clear. You can assume that the tutor always knows the correct solution. You should answer only "Yes" or "No" without explanations. You should answer "Yes" if the Tutor gives away the correct solution directly and explicitly. Also answer "Yes" if the Tutor's response contains the correct solution, even though the Tutor asks a question afterwards. You should answer "No" in all of the following situations: All situations where the Tutor doesn't give away the correct solution directly. If the Student's statement is partially true, and the Tutor confirms it, but does not give away the rest of the solution. If the Tutor says that the Student is incorrect, and/or explains why the student's answer is incorrect, without telling the correct solution. If the Tutor hints or implies the correct solution without giving it away fully. If the Tutor asks a question without saying the correct solution. If the Tutor asks the Student to explain their solution or to try again.
MESSAGE user TUTOR: Yes correct . TUTOR: The other end of the crayon is at 4, which means the other end of the crayon is at 4 centimeters. TUTOR: What is the value of 4 centimeters  - 0 centimeters ? STUDENT: 40 TUTOR: Hm, not quite. Our goal is to figure out how long the crayon is. Do you know how long the crayon is?
MESSAGE assistant No
MESSAGE user TUTOR: Here is the first question. TUTOR: In this question, we are asked to find the total minutes of the game. TUTOR: How many minutes is 1 hour? STUDENT: 59 minutes TUTOR: Very close! an hour is 60 minutes
MESSAGE assistant Yes
PARAMETER temperature 0
'''


bridge_1 = []
bridge_2 = []
mathdial = []

for index, row in data.iterrows():
    #if conversation id contains two underscore
    if row['conversation_id'].count('_') == 2:
        if row['conversation_id'].endswith('1'):
            bridge_1.append(index)
        if row['conversation_id'].endswith('2'):
            bridge_2.append(index)
    elif row['conversation_id'].count('_') == 1:
        mathdial.append(index)

# Use the formatted model name with the suffix
ollama.create(model=f'rubric1_{model_name_suffix}', modelfile=modelfile)


i, j, k, l = 0, 0, 0, 0
bridge_1_yes = 0
bridge_1_no = 0
bridge_1_org_yes = 0
bridge_1_org_no = 0

bridge_2_yes = 0
bridge_2_no = 0
bridge_2_org_yes = 0
bridge_2_org_no = 0

mathdial_yes = 0
mathdial_no = 0
mathdial_org_yes = 0
mathdial_org_no = 0


# Iterate through each row in the DataFrame
for index, row in data.iterrows():
    # Extract conversation text and ID from the row
    rubric_1 = row['rubric_1']
    if pd.isna(rubric_1): continue

    conversation_text = row['text']
    conversation_id = row['conversation_id']
    
    full_conversation = [{"role": "user", "content": conversation_text}]

    response = ollama.chat(model=f'rubric1_{model_name_suffix}', messages=full_conversation)

    if index in bridge_1:
        if rubric_1 == 'Yes':
            bridge_1_org_yes += 1
        elif rubric_1 == 'No':
            bridge_1_org_no += 1
        if response['message']['content'] == 'Yes':
            bridge_1_yes += 1
        elif response['message']['content'] == 'No':
            bridge_1_no += 1
    
    if index in bridge_2:
        if rubric_1 == 'Yes':
            bridge_2_org_yes += 1
        elif rubric_1 == 'No':
            bridge_2_org_no += 1
        if response['message']['content'] == 'Yes':
            bridge_2_yes += 1
        elif response['message']['content'] == 'No':
            bridge_2_no += 1
    
    if index in mathdial:
        if rubric_1 == 'Yes':
            mathdial_org_yes += 1
        elif rubric_1 == 'No':
            mathdial_org_no += 1
        if response['message']['content'] == 'Yes':
            mathdial_yes += 1
        elif response['message']['content'] == 'No':
            mathdial_no += 1

    if rubric_1 != response['message']['content']:
        j += 1
        if rubric_1 == 'Yes' and response['message']['content'] == 'No':
            k += 1
        if rubric_1 == 'No' and response['message']['content'] == 'Yes':
            l += 1
    
    
    i += 1

print(f"Number of conversations: {i}")

print(f"Number of wrong answers for rubric1_{model_name_suffix}: {j}")
print(f"Number of No answers where correct answer is Yes for rubric1_{model_name_suffix}: {k}")
print(f"Number of Yes answers where correct answer is No for rubric1_{model_name_suffix}: {l}")

print(f"Bridge 1 Yes: {bridge_1_yes}")
print(f"Bridge 1 No: {bridge_1_no}")
print(f"Bridge 1 Original Yes: {bridge_1_org_yes}")
print(f"Bridge 1 Original No: {bridge_1_org_no}")

print(f"Bridge 2 Yes: {bridge_2_yes}")
print(f"Bridge 2 No: {bridge_2_no}")
print(f"Bridge 2 Original Yes: {bridge_2_org_yes}")
print(f"Bridge 2 Original No: {bridge_2_org_no}")

print(f"Mathdial Yes: {mathdial_yes}")
print(f"Mathdial No: {mathdial_no}")
print(f"Mathdial Original Yes: {mathdial_org_yes}")
print(f"Mathdial Original No: {mathdial_org_no}")