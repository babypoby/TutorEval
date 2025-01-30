import ollama
import pandas as pd
import argparse


# Set up argument parser
parser = argparse.ArgumentParser(description='Run Ollama model evaluation with a specified model.')
parser.add_argument('model_from', type=str, help='The model FROM parameter to use, e.g., "llama3:70b"')
args = parser.parse_args()

# Get the model FROM parameter from the command line argument
model_from = args.model_from

# Replace invalid characters for model naming
model_name_suffix = model_from.replace(':', '_').replace('/', '_')

data = pd.read_csv('data_combined.csv')


modelfile= f'''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor has a positive tone at their last utterance. The Tutor must be highly positive, enthusiastic and encouraging in their use of language. For each conversation, only answer "Yes" or "No". Answer "Yes" if: The Tutor is explicitly using highly positive, enthusiastic and encouraging and motivating language. Tutor uses positive expressions like "great try!", "you're almost there!". Answer "No" if: The Tutor has a neutral tone. The Tutor is somewhat positive. The Tutor is asking questions or making suggestions for the student, without using explicit positive language. Tutor uses only somewhat positive expressions like "that works." or "good try". Note that you should not imply the positivity of the Tutor's tone from the given text. Judge only based on the explicitly chosen words, expressions and punctuation marks. 
MESSAGE user TUTOR: Yes correct . TUTOR: The other end of the crayon is at 4, which means the other end of the crayon is at 4 centimeters. TUTOR: What is the value of 4 centimeters  - 0 centimeters ? STUDENT: 40 TUTOR: Hm, not quite. Our goal is to figure out how long the crayon is. Do you know how long the crayon is?
MESSAGE assistant No
MESSAGE user TUTOR: Here is the first question. TUTOR: In this question, we are asked to find the total minutes of the game. TUTOR: How many minutes is 1 hour? STUDENT: 59 minutes TUTOR: Very close! an hour is 60 minutes
MESSAGE assistant Yes
PARAMETER temperature 0
'''

modelfile_basic = f'''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor has a positive tone at their specific point of progress in the conversation. For each conversation, only answer „Yes" or „No". Answer „Yes" if the Tutor is highly positive, enthusiastic and encouraging. Answer „No“  if the Tutor is neutral or somewhat positive.
MESSAGE user TUTOR: Yes correct . TUTOR: The other end of the crayon is at 4, which means the other end of the crayon is at 4 centimeters. TUTOR: What is the value of 4 centimeters  - 0 centimeters ? STUDENT: 40 TUTOR: Hm, not quite. Our goal is to figure out how long the crayon is. Do you know how long the crayon is?
MESSAGE assistant No
MESSAGE user TUTOR: Here is the first question. TUTOR: In this question, we are asked to find the total minutes of the game. TUTOR: How many minutes is 1 hour? STUDENT: 59 minutes TUTOR: Very close! an hour is 60 minutes
MESSAGE assistant Yes
PARAMETER temperature 0
'''

data = pd.read_csv('data_combined.csv')
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

bridge_1_yes_basic = 0
bridge_1_no_basic = 0
bridge_1_org_yes_basic = 0
bridge_1_org_no_basic = 0

bridge_2_yes_basic = 0
bridge_2_no_basic = 0
bridge_2_org_yes_basic = 0
bridge_2_org_no_basic = 0

mathdial_yes_basic = 0
mathdial_no_basic = 0
mathdial_org_yes_basic = 0
mathdial_org_no_basic = 0


ollama.create(model=f'rubric4_{model_name_suffix}', modelfile=modelfile)
ollama.create(model=f'rubric4_basic_{model_name_suffix}', modelfile=modelfile_basic)


i,j,k,l = 0,0,0,0
j_bas, k_bas, l_bas = 0,0,0

for index, row in data.iterrows():
    rubric_4 = row['rubric_4']
    if pd.isna(rubric_4) : continue

    conversation_text = row['text']
    conversation_id = row['conversation_id']
    
    full_conversation = [{"role": "user", "content": conversation_text}]
    response = ollama.chat(model=f'rubric4_{model_name_suffix}', messages=full_conversation)
    response_basic = ollama.chat(model=f'rubric4_basic_{model_name_suffix}', messages=full_conversation)

    if index in bridge_1:
        if response['message']['content'] == 'Yes':
            bridge_1_yes += 1
        elif response['message']['content'] == 'No':
            bridge_1_no += 1
        if rubric_4 == 'Yes':
            bridge_1_org_yes += 1
        elif rubric_4 == 'No':
            bridge_1_org_no += 1

        if response_basic['message']['content'] == 'Yes':
            bridge_1_yes_basic += 1
        elif response_basic['message']['content'] == 'No':
            bridge_1_no_basic += 1
        if rubric_4 == 'Yes':
            bridge_1_org_yes_basic += 1
        elif rubric_4 == 'No':
            bridge_1_org_no_basic += 1
    
    if index in bridge_2:
        if response['message']['content'] == 'Yes':
            bridge_2_yes += 1
        elif response['message']['content'] == 'No':
            bridge_2_no += 1
        if rubric_4 == 'Yes':
            bridge_2_org_yes += 1
        elif rubric_4 == 'No':
            bridge_2_org_no += 1

        if response_basic['message']['content'] == 'Yes':
            bridge_2_yes_basic += 1
        elif response_basic['message']['content'] == 'No':
            bridge_2_no_basic += 1
        if rubric_4 == 'Yes':
            bridge_2_org_yes_basic += 1
        elif rubric_4 == 'No':
            bridge_2_org_no_basic += 1
    
    if index in mathdial:
        if response['message']['content'] == 'Yes':
            mathdial_yes += 1
        elif response['message']['content'] == 'No':
            mathdial_no += 1
        if rubric_4 == 'Yes':
            mathdial_org_yes += 1
        elif rubric_4 == 'No':
            mathdial_org_no += 1

        if response_basic['message']['content'] == 'Yes':
            mathdial_yes_basic += 1
        elif response_basic['message']['content'] == 'No':
            mathdial_no_basic += 1
        if rubric_4 == 'Yes':
            mathdial_org_yes_basic += 1
        elif rubric_4 == 'No':
            mathdial_org_no_basic += 1


    if rubric_4 != response['message']['content']:
        j += 1
        if rubric_4 == 'Yes' and response['message']['content'] == 'No':
            k += 1
        if rubric_4 == 'No' and response['message']['content'] == 'Yes':
            l += 1
    
    if rubric_4 != response_basic['message']['content']:
        j_bas += 1
        if rubric_4 == 'Yes' and response_basic['message']['content'] == 'No':
            k_bas += 1
        if rubric_4 == 'No' and response_basic['message']['content'] == 'Yes':
            l_bas += 1

    
    i += 1


print (f"Toal number of conversations: {i}")

print(f"Number of wrong answers for rubric4_{model_name_suffix}: {j}")
print(f"Number of wrong answers for rubric4_basic_{model_name_suffix}: {j_bas}")


print(f"Number of No answers where correct answer is Yes for rubric4_{model_name_suffix}: {k}")
print(f"Number of No answers where correct answer is Yes for rubric4_basic_{model_name_suffix}: {k_bas}")


print(f"Number of Yes answers where correct answer is No for rubric4_{model_name_suffix}: {l}")
print(f"Number of Yes answers where correct answer is No for rubric4_basic_{model_name_suffix}: {l_bas}")

print('Bridge 1 Yes:', bridge_1_yes)
print('Bridge 1 No:', bridge_1_no)
print('Bridge 1 Original Yes:', bridge_1_org_yes)
print('Bridge 1 Original No:', bridge_1_org_no)

print('Bridge 2 Yes:', bridge_2_yes)
print('Bridge 2 No:', bridge_2_no)
print('Bridge 2 Original Yes:', bridge_2_org_yes)
print('Bridge 2 Original No:', bridge_2_org_no)

print('Mathdial Yes:', mathdial_yes)
print('Mathdial No:', mathdial_no)
print('Mathdial Original Yes:', mathdial_org_yes)
print('Mathdial Original No:', mathdial_org_no)

print('Bridge 1 Yes Basic:', bridge_1_yes_basic)
print('Bridge 1 No Basic:', bridge_1_no_basic)
print('Bridge 1 Original Yes Basic:', bridge_1_org_yes_basic)
print('Bridge 1 Original No Basic:', bridge_1_org_no_basic)

print('Bridge 2 Yes Basic:', bridge_2_yes_basic)
print('Bridge 2 No Basic:', bridge_2_no_basic)
print('Bridge 2 Original Yes Basic:', bridge_2_org_yes_basic)
print('Bridge 2 Original No Basic:', bridge_2_org_no_basic)

print('Mathdial Yes Basic:', mathdial_yes_basic)
print('Mathdial No Basic:', mathdial_no_basic)
print('Mathdial Original Yes Basic:', mathdial_org_yes_basic)
print('Mathdial Original No Basic:', mathdial_org_no_basic)

