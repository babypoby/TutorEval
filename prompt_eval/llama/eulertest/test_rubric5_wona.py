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

modelfile= '''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor point out the Student's mistake at their last utterance. You may assume that the student's answer contains an error. You can always assume that the Tutor knows the correct answer. You should answer only „Yes“ or „No“. Answer „Yes“ in the following situations: The Tutor points out the mistake or opportunities for improvement. The Tutor identifies and addresses the Student's misconceptions. The Tutor asks a question which draws attention to the mistake. The Tutor points out the Student's error through a practice question or an example. Answer „No“ in the following situations: The Tutor states that the Student's statement is right even though it is not. The Tutor does not point out the mistake directly or not at all. The Tutor gives the right answer without pointing out what was wrong. The Tutor states that the Student's statement is wrong without pointing out what was wrong. 
MESSAGE user TUTOR: Yes correct . TUTOR: The other end of the crayon is at 4, which means the other end of the crayon is at 4 centimeters. TUTOR: What is the value of 4 centimeters  - 0 centimeters ? STUDENT: 40 TUTOR: Hm, not quite. Our goal is to figure out how long the crayon is. Do you know how long the crayon is?
MESSAGE assistant No
MESSAGE user TUTOR: Here is the first question. TUTOR: In this question, we are asked to find the total minutes of the game. TUTOR: How many minutes is 1 hour? STUDENT: 59 minutes TUTOR: Very close! an hour is 60 minutes
MESSAGE assistant Yes
PARAMETER temperature 0
'''

modelfile_basic= '''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor point out the Student's mistake at their specific point of progress in the conversation. You may assume that the student's answer contains an error. You can always assume that the Tutor knows the correct answer. You should answer only „Yes“ or „No“. Answer „Yes“ in the following situations: The Tutor points out the mistake or opportunities for improvement. The Tutor identifies and addresses the Student's misconceptions. The Tutor asks a question which draws attention to the mistake. Answer „No“ in the following situations: The Tutor states that the Student's statement is right even though it is not. The Tutor does not point out the mistake directly or not at all. The Tutor gives the right answer without pointing out what was wrong. The Tutor states that the Student's statement is wrong without pointing out what was wrong.
MESSAGE user TUTOR: Yes correct . TUTOR: The other end of the crayon is at 4, which means the other end of the crayon is at 4 centimeters. TUTOR: What is the value of 4 centimeters  - 0 centimeters ? STUDENT: 40 TUTOR: Hm, not quite. Our goal is to figure out how long the crayon is. Do you know how long the crayon is?
MESSAGE assistant No
MESSAGE user TUTOR: Here is the first question. TUTOR: In this question, we are asked to find the total minutes of the game. TUTOR: How many minutes is 1 hour? STUDENT: 59 minutes TUTOR: Very close! an hour is 60 minutes
MESSAGE assistant Yes
PARAMETER temperature 0
'''

modelfile_nex= '''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor point out the Student's mistake at their last utterance. You may assume that the student's answer contains an error. You can always assume that the Tutor knows the correct answer. You should answer only „Yes“ or „No“. Answer „Yes“ in the following situations: The Tutor points out the mistake or opportunities for improvement. The Tutor identifies and addresses the Student's misconceptions. The Tutor asks a question which draws attention to the mistake. The Tutor points out the Student's error through a practice question or an example. Answer „No“ in the following situations: The Tutor states that the Student's statement is right even though it is not. The Tutor does not point out the mistake directly or not at all. The Tutor gives the right answer without pointing out what was wrong. The Tutor states that the Student's statement is wrong without pointing out what was wrong. 
PARAMETER temperature 0
'''

modelfile_basic_nex= '''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor point out the Student's mistake at their specific point of progress in the conversation. You may assume that the student's answer contains an error. You can always assume that the Tutor knows the correct answer. You should answer only „Yes“ or „No“. Answer „Yes“ in the following situations: The Tutor points out the mistake or opportunities for improvement. The Tutor identifies and addresses the Student's misconceptions. The Tutor asks a question which draws attention to the mistake. Answer „No“ in the following situations: The Tutor states that the Student's statement is right even though it is not. The Tutor does not point out the mistake directly or not at all. The Tutor gives the right answer without pointing out what was wrong. The Tutor states that the Student's statement is wrong without pointing out what was wrong.
PARAMETER temperature 0
'''

ollama.create(model=f'rubric5_{model_name_suffix}', modelfile=modelfile)
ollama.create(model=f'rubric5_basic_{model_name_suffix}', modelfile=modelfile_basic)
ollama.create(model=f'rubric5_nex_{model_name_suffix}', modelfile=modelfile_nex)
ollama.create(model=f'rubric5_basic_nex_{model_name_suffix}', modelfile=modelfile_basic_nex)

i,j,k,l = 0,0,0,0
j_bas, k_bas, l_bas = 0,0,0
j_nex, k_nex, l_nex = 0,0,0
j_bas_nex, k_bas_nex, l_bas_nex = 0,0,0

for index,row in data.iterrows():
    rubric_5 = row['rubric_5']
    if pd.isna(rubric_5): continue

    conversation_text = row['text']
    conversation_id = row['conversation_id']

    full_conversation = [{"role": "user", "content": conversation_text}]
    response = ollama.chat(model=f'rubric5_{model_name_suffix}', messages=full_conversation)
    response_basic = ollama.chat(model=f'rubric5_basic_{model_name_suffix}', messages=full_conversation)
    response_nex = ollama.chat(model=f'rubric5_nex_{model_name_suffix}', messages=full_conversation)
    response_basic_nex = ollama.chat(model=f'rubric5_basic_nex_{model_name_suffix}', messages=full_conversation)


    if rubric_5 != response['message']['content']:
        j += 1
        if rubric_5 == 'Yes' and response['message']['content'] == 'No':
            k += 1
        if rubric_5 == 'No' and response['message']['content'] == 'Yes':
            l += 1
    
    if rubric_5 != response_basic['message']['content']:
        j_bas += 1
        if rubric_5 == 'Yes' and response_basic['message']['content'] == 'No':
            k_bas += 1
        if rubric_5 == 'No' and response_basic['message']['content'] == 'Yes':
            l_bas += 1

    if rubric_5 != response_nex['message']['content']:
        j_nex += 1
        if rubric_5 == 'Yes' and response_nex['message']['content'] == 'No':
            k_nex += 1
        if rubric_5 == 'No' and response_nex['message']['content'] == 'Yes':
            l_nex += 1
    
    if rubric_5 != response_basic_nex['message']['content']:
        j_bas_nex += 1
        if rubric_5 == 'Yes' and response_basic_nex['message']['content'] == 'No':
            k_bas_nex += 1
        if rubric_5 == 'No' and response_basic_nex['message']['content'] == 'Yes':
            l_bas_nex += 1
    
    i += 1


    
print (f"Total number of conversations: {i}")

print(f"Number of wrong answers for rubric5_{model_name_suffix}: {j}")
print(f"Number of wrong answers for rubric5_basic_{model_name_suffix}: {j_bas}")
print(f"Number of wrong answers for rubric5_nex_{model_name_suffix}: {j_nex}")
print(f"Number of wrong answers for rubric5_basic_nex_{model_name_suffix}: {j_bas_nex}")

print(f"Number of No answers where correct answer is Yes for rubric5_{model_name_suffix}: {k}")
print(f"Number of No answers where correct answer is Yes for rubric5_basic_{model_name_suffix}: {k_bas}")
print(f"Number of No answers where correct answer is Yes for rubric5_nex_{model_name_suffix}: {k_nex}")
print(f"Number of No answers where correct answer is Yes for rubric5_basic_nex_{model_name_suffix}: {k_bas_nex}")

print(f"Number of Yes answers where correct answer is No for rubric5_{model_name_suffix}: {l}")
print(f"Number of Yes answers where correct answer is No for rubric5_basic_{model_name_suffix}: {l_bas}")
print(f"Number of Yes answers where correct answer is No for rubric5_nex_{model_name_suffix}: {l_nex}")
print(f"Number of Yes answers where correct answer is No for rubric5_basic_nex_{model_name_suffix}: {l_bas_nex}")
