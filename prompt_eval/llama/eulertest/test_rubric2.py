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
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor should always promote active engagement. This means that the Tutor should try to encourage the Student to engage actively instead of doing the work for them or giving them no chance to participate. For the given conversation, your task is to determine if the Tutor promotes active engagement at their last utterance. You should answer "Yes" or "No". You should answer "Yes" in the following situations: All situations where the tutor asks or tells the student to do something actively or asks a question. If the Tutor asks practice questions. If the Tutor asks follow up questions. If the Tutor tells the Student to try something by themselves. If the Tutor asks the Student to explain their reasoning. If the Tutor asks the Student to show their work. If the Tutor asks the Student to recheck their answer. If the Tutor asks the Student to talk through their answer. If the Tutor asks the student whether they would like to learn more. If the Tutor asks whether the student understood. Answer "No" in the following situations: If the Tutor does not ask the Student to do anything actively and also not asks a question. If the Tutor simply comments on the Student's answer like "good job" or "so close" or "that is incorrect" without actively asking the student to do something. If the Tutor explains or states a concept or an answer without asking the student to do something.
MESSAGE user TUTOR: Yes correct . TUTOR: The other end of the crayon is at 4, which means the other end of the crayon is at 4 centimeters. TUTOR: What is the value of 4 centimeters  - 0 centimeters ? STUDENT: 40 TUTOR: Hm, not quite. Our goal is to figure out how long the crayon is. Do you know how long the crayon is?
MESSAGE assistant Yes
MESSAGE user TUTOR: Here is the first question. TUTOR: In this question, we are asked to find the total minutes of the game. TUTOR: How many minutes is 1 hour? STUDENT: 59 minutes TUTOR: Very close! an hour is 60 minutes
MESSAGE assistant No
PARAMETER temperature 0
'''

modelfile_basic = f'''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor should always promote active engagement. The Tutor can promote active engagement from the Student by asking follow-up questions to dig deeper, asking whether the Student would like to learn more, asking the Student to try something for themselves, and providing practice problems. For the given conversation, your task is to determine if the Tutor promotes active engagement at their specific point of progress in the conversation. You should answer "Yes" or "No".
MESSAGE user TUTOR: Yes correct . TUTOR: The other end of the crayon is at 4, which means the other end of the crayon is at 4 centimeters. TUTOR: What is the value of 4 centimeters  - 0 centimeters ? STUDENT: 40 TUTOR: Hm, not quite. Our goal is to figure out how long the crayon is. Do you know how long the crayon is?
MESSAGE assistant Yes
MESSAGE user TUTOR: Here is the first question. TUTOR: In this question, we are asked to find the total minutes of the game. TUTOR: How many minutes is 1 hour? STUDENT: 59 minutes TUTOR: Very close! an hour is 60 minutes
MESSAGE assistant No
PARAMETER temperature 0
'''

modelfile_nex= f'''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor should always promote active engagement. This means that the Tutor should try to encourage the Student to engage actively instead of doing the work for them or giving them no chance to participate. For the given conversation, your task is to determine if the Tutor promotes active engagement at their last utterance. You should answer "Yes" or "No". You should answer "Yes" in the following situations: All situations where the tutor asks or tells the student to do something actively or asks a question. If the Tutor asks practice questions. If the Tutor asks follow up questions. If the Tutor tells the Student to try something by themselves. If the Tutor asks the Student to explain their reasoning. If the Tutor asks the Student to show their work. If the Tutor asks the Student to recheck their answer. If the Tutor asks the Student to talk through their answer. If the Tutor asks the student whether they would like to learn more. If the Tutor asks whether the student understood. Answer "No" in the following situations: If the Tutor does not ask the Student to do anything actively and also not asks a question. If the Tutor simply comments on the Student's answer like "good job" or "so close" or "that is incorrect" without actively asking the student to do something. If the Tutor explains or states a concept or an answer without asking the student to do something.
PARAMETER temperature 0
'''

modelfile_basic_nex = f'''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor should always promote active engagement. The Tutor can promote active engagement from the Student by asking follow-up questions to dig deeper, asking whether the Student would like to learn more, asking the Student to try something for themselves, and providing practice problems. For the given conversation, your task is to determine if the Tutor promotes active engagement at their specific point of progress in the conversation. You should answer "Yes" or "No".
PARAMETER temperature 0
'''

ollama.create(model=f'rubric2_{model_name_suffix}', modelfile=modelfile)
ollama.create(model=f'rubric2_basic_{model_name_suffix}', modelfile=modelfile_basic)
ollama.create(model=f'rubric2_nex_{model_name_suffix}', modelfile=modelfile_nex)
ollama.create(model=f'rubric2_basic_nex_{model_name_suffix}', modelfile=modelfile_basic_nex)

i,j,k,l = 0,0,0,0
j_bas, k_bas, l_bas = 0,0,0
j_nex, k_nex, l_nex = 0,0,0
j_bas_nex, k_bas_nex, l_bas_nex = 0,0,0


# Iterate through each row in the DataFrame
for index, row in data.iterrows():
    # Extract conversation text and ID from the row
    rubric_2 = row['rubric_2']
    if pd.isna(rubric_2) : continue

    conversation_text = row['text']
    conversation_id = row['conversation_id']
    
    full_conversation = [{"role": "user", "content": conversation_text}]
    response = ollama.chat(model=f'rubric2_{model_name_suffix}', messages=full_conversation)
    response_basic = ollama.chat(model=f'rubric2_basic_{model_name_suffix}', messages=full_conversation)
    response_nex = ollama.chat(model=f'rubric2_nex_{model_name_suffix}', messages=full_conversation)
    response_basic_nex = ollama.chat(model=f'rubric2_basic_nex_{model_name_suffix}', messages=full_conversation)

    if rubric_2 != response['message']['content']:
        j += 1
        if rubric_2 == 'Yes' and response['message']['content'] == 'No':
            k += 1
        if rubric_2 == 'No' and response['message']['content'] == 'Yes':
            l += 1
    
    if rubric_2 != response_basic['message']['content']:
        j_bas += 1
        if rubric_2 == 'Yes' and response_basic['message']['content'] == 'No':
            k_bas += 1
        if rubric_2 == 'No' and response_basic['message']['content'] == 'Yes':
            l_bas += 1
    
    if rubric_2 != response_nex['message']['content']:
        j_nex += 1
        if rubric_2 == 'Yes' and response_nex['message']['content'] == 'No':
            k_nex += 1
        if rubric_2 == 'No' and response_nex['message']['content'] == 'Yes':
            l_nex += 1
    
    if rubric_2 != response_basic_nex['message']['content']:
        j_bas_nex += 1
        if rubric_2 == 'Yes' and response_basic_nex['message']['content'] == 'No':
            k_bas_nex += 1
        if rubric_2 == 'No' and response_basic_nex['message']['content'] == 'Yes':
            l_bas_nex += 1
    
    i += 1

print(f"Number of conversations: {i}")

print(f"Number of wrong answers for rubric2_{model_name_suffix}: {j}")
print(f"Number of wrong answers for rubric2_basic_{model_name_suffix}: {j_bas}")
print(f"Number of wrong answers for rubric2_nex_{model_name_suffix}: {j_nex}")
print(f"Number of wrong answers for rubric2_basic_nex_{model_name_suffix}: {j_bas_nex}")

print(f"Number of No answers where correct answer is Yes for rubric2_{model_name_suffix}: {k}")
print(f"Number of No answers where correct answer is Yes for rubric2_basic_{model_name_suffix}: {k_bas}")
print(f"Number of No answers where correct answer is Yes for rubric2_nex_{model_name_suffix}: {k_nex}")
print(f"Number of No answers where correct answer is Yes for rubric2_basic_nex_{model_name_suffix}: {k_bas_nex}")

print(f"Number of Yes answers where correct answer is No for rubric2_{model_name_suffix}: {l}")
print(f"Number of Yes answers where correct answer is No for rubric2_basic_{model_name_suffix}: {l_bas}")
print(f"Number of Yes answers where correct answer is No for rubric2_nex_{model_name_suffix}: {l_nex}")
