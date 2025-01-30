import argparse
import ollama
import pandas as pd

# Set up argument parser
#parser = argparse.ArgumentParser(description='Run Ollama model evaluation with a specified model.')
#parser.add_argument('model_from', type=str, help='The model FROM parameter to use, e.g., "llama3:70b"')
#args = parser.parse_args()

# Get the model FROM parameter from the command line argument
model_from = "llama3.2:1b-instruct-fp16"

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

modelfile_basic = f'''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor must never give away the correct solution. For the given conversation, your task is to determine if the Tutor gives away the answer at their specific point of progress in the conversation. In every conversation, the student is currently incorrect. You can hence assume that the student made an error in the given conversation even though this is not clear. You can assume that the tutor always knows the correct solution. You should answer only "Yes" or "No" without explanations. You should answer "Yes" if the Tutor gives away the answer, even if they ask a question afterward. Also answer "Yes" if the Student’s statement is partially true, and the Tutor confirms it, but does not give away the full answer. You should answer "No" if the Tutor doesn’t give away the answer. Also answer "No" if the Student’s statement is partially true, and the Tutor confirms it, but does not give away the full answer.
MESSAGE user TUTOR: Yes correct . TUTOR: The other end of the crayon is at 4, which means the other end of the crayon is at 4 centimeters. TUTOR: What is the value of 4 centimeters  - 0 centimeters ? STUDENT: 40 TUTOR: Hm, not quite. Our goal is to figure out how long the crayon is. Do you know how long the crayon is?
MESSAGE assistant No
MESSAGE user TUTOR: Here is the first question. TUTOR: In this question, we are asked to find the total minutes of the game. TUTOR: How many minutes is 1 hour? STUDENT: 59 minutes TUTOR: Very close! an hour is 60 minutes
MESSAGE assistant Yes
PARAMETER temperature 0
'''


modelfile_nex = f'''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor must never give away the correct solution. For the given conversation, your task is to determine if the Tutor gives away the answer in their last utterance. In every conversation, the student is currently incorrect. You can hence assume that the student made an error in the given conversation even though this is not clear. You can assume that the tutor always knows the correct solution. You should answer only "Yes" or "No" without explanations. You should answer "Yes" if the Tutor gives away the correct solution directly and explicitly. Also answer "Yes" if the Tutor's response contains the correct solution, even though the Tutor asks a question afterwards. You should answer "No" in all of the following situations: All situations where the Tutor doesn't give away the correct solution directly. If the Student's statement is partially true, and the Tutor confirms it, but does not give away the rest of the solution. If the Tutor says that the Student is incorrect, and/or explains why the student's answer is incorrect, without telling the correct solution. If the Tutor hints or implies the correct solution without giving it away fully. If the Tutor asks a question without saying the correct solution. If the Tutor asks the Student to explain their solution or to try again.
PARAMETER temperature 0
'''

modelfile_basic_nex = f'''
FROM {model_from}
SYSTEM You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor must never give away the correct solution. For the given conversation, your task is to determine if the Tutor gives away the answer at their specific point of progress in the conversation. In every conversation, the student is currently incorrect. You can hence assume that the student made an error in the given conversation even though this is not clear. You can assume that the tutor always knows the correct solution. You should answer only "Yes" or "No" without explanations. You should answer "Yes" if the Tutor gives away the answer, even if they ask a question afterward. Also answer "Yes" if the Student’s statement is partially true, and the Tutor confirms it, but does not give away the full answer. You should answer "No" if the Tutor doesn’t give away the answer. Also answer "No" if the Student’s statement is partially true, and the Tutor confirms it, but does not give away the full answer.
PARAMETER temperature 0
'''


# Use the formatted model name with the suffix
ollama.create(model=f'rubric1_{model_name_suffix}', modelfile=modelfile)
ollama.create(model=f'rubric1_basic_{model_name_suffix}', modelfile=modelfile_basic)
ollama.create(model=f'rubric1_nex_{model_name_suffix}', modelfile=modelfile_nex)
ollama.create(model=f'rubric1_basic_nex_{model_name_suffix}', modelfile=modelfile_basic_nex)

i, j, k, l = 0, 0, 0, 0
j_bas, k_bas, l_bas = 0, 0, 0
j_nex, k_nex, l_nex = 0, 0, 0
j_bas_nex, k_bas_nex, l_bas_nex = 0, 0, 0

# Iterate through each row in the DataFrame
for index, row in data.iterrows():
    rubric_1 = row['rubric_1']
    if pd.isna(rubric_1): continue
    print("Processing conversation", index)
    print("Conversation id:", row['conversation_id'])
    # Extract conversation text and ID from the row


    conversation_text = row['text']
    conversation_id = row['conversation_id']

    full_conversation = [{"role": "user", "content": conversation_text}]


    response = ollama.chat(model=f'rubric1_{model_name_suffix}', messages=full_conversation)
    print(response)

    response_basic = ollama.chat(model=f'rubric1_basic_{model_name_suffix}', messages=full_conversation)
    print(response_basic)
    #response_nex = ollama.chat(model=f'rubric1_nex_{model_name_suffix}', messages=full_conversation)
    #print(response_nex)
    #response_basic_nex = ollama.chat(model=f'rubric1_basic_nex_{model_name_suffix}', messages=full_conversation)
    #print(response_basic_nex)


    if rubric_1 != response['message']['content']:
        print("Wrong answer 1")
        j += 1
        if rubric_1 == 'Yes' and response['message']['content'] == 'No':
            k += 1
        if rubric_1 == 'No' and response['message']['content'] == 'Yes':
            l += 1

    if rubric_1 != response_basic['message']['content']:
        print("Wrong answer 2")
        j_bas += 1
        if rubric_1 == 'Yes' and response_basic['message']['content'] == 'No':
            k_bas += 1
        if rubric_1 == 'No' and response_basic['message']['content'] == 'Yes':
            l_bas += 1

    '''if rubric_1 != response_nex['message']['content']:
        print("Wrong answer 3")
        j_nex += 1
        if rubric_1 == 'Yes' and response_nex['message']['content'] == 'No':
            k_nex += 1
        if rubric_1 == 'No' and response_nex['message']['content'] == 'Yes':
            l_nex += 1

    if rubric_1 != response_basic_nex['message']['content']:
        print("Wrong answer 4")
        j_bas_nex += 1
        if rubric_1 == 'Yes' and response_basic_nex['message']['content'] == 'No':
            k_bas_nex += 1
        if rubric_1 == 'No' and response_basic_nex['message']['content'] == 'Yes':
            l_bas_nex += 1'''
    
    i += 1

print(f"Number of conversations: {i}")

print(f"Number of wrong answers for rubric1_{model_name_suffix}: {j}")
print(f"Number of wrong answers for rubric1_basic_{model_name_suffix}: {j_bas}")
print(f"Number of wrong answers for rubric1_nex_{model_name_suffix}: {j_nex}")
print(f"Number of wrong answers for rubric1_basic_nex_{model_name_suffix}: {j_bas_nex}")

print(f"Number of No answers where correct answer is Yes for rubric1_{model_name_suffix}: {k}")
print(f"Number of No answers where correct answer is Yes for rubric1_basic_{model_name_suffix}: {k_bas}")
print(f"Number of No answers where correct answer is Yes for rubric1_nex_{model_name_suffix}: {k_nex}")
print(f"Number of No answers where correct answer is Yes for rubric1_basic_nex_{model_name_suffix}: {k_bas_nex}")

print(f"Number of Yes answers where correct answer is No for rubric1_{model_name_suffix}: {l}")
print(f"Number of Yes answers where correct answer is No for rubric1_basic_{model_name_suffix}: {l_bas}")
print(f"Number of Yes answers where correct answer is No for rubric1_nex_{model_name_suffix}: {l_nex}")
print(f"Number of Yes answers where correct answer is No for rubric1_basic_nex_{model_name_suffix}: {l_bas_nex}")