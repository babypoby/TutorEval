import pandas as pd
import json


data = pd.read_csv('data_combined.csv')

example_1 = '''TUTOR: Yes correct . TUTOR: The other end of the crayon is at 4, which means the other end of the crayon is at 4 centimeters. TUTOR: What is the value of 4 centimeters  - 0 centimeters ? STUDENT: 40 TUTOR: Hm, not quite. Our goal is to figure out how long the crayon is. Do you know how long the crayon is?'''
example_2 = '''TUTOR: Here is the first question. TUTOR: In this question, we are asked to find the total minutes of the game. TUTOR: How many minutes is 1 hour? STUDENT: 59 minutes TUTOR: Very close! an hour is 60 minutes'''

rubric1_prompt = '''You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor must never give away the correct solution. For the given conversation, your task is to determine if the Tutor gives away the answer in their last utterance. In every conversation, the student is currently incorrect. You can hence assume that the student made an error in the given conversation even though this is not clear. You can assume that the tutor always knows the correct solution. You should answer only "Yes" or "No" without explanations. You should answer "Yes" if the Tutor gives away the correct solution directly and explicitly. Also answer "Yes" if the Tutor's response contains the correct solution, even though the Tutor asks a question afterwards. You should answer "No" in all of the following situations: All situations where the Tutor doesn't give away the correct solution directly. If the Student's statement is partially true, and the Tutor confirms it, but does not give away the rest of the solution. If the Tutor says that the Student is incorrect, and/or explains why the student's answer is incorrect, without telling the correct solution. If the Tutor hints or implies the correct solution without giving it away fully. If the Tutor asks a question without saying the correct solution. If the Tutor asks the Student to explain their solution or to try again.'''
rubric1_prompt_basic = '''You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor must never give away the correct solution. For the given conversation, your task is to determine if the Tutor gives away the answer at their specific point of progress in the conversation. In every conversation, the student is currently incorrect. You can hence assume that the student made an error in the given conversation even though this is not clear. You can assume that the tutor always knows the correct solution. You should answer only "Yes" or "No". You should answer "Yes" if the Tutor gives away the answer, even if they ask a question afterward. Also answer "Yes" if the Student’s statement is partially true, and the Tutor confirms it, but does not give away the full answer. You should answer "No" if the Tutor doesn’t give away the answer. Also answer "No" if the Student’s statement is partially true, and the Tutor confirms it, but does not give away the full answer.'''

rubric2_prompt = '''You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor should always promote active engagement. This means that the Tutor should try to encourage the Student to engage actively instead of doing the work for them or giving them no chance to participate. For the given conversation, your task is to determine if the Tutor promotes active engagement at their last utterance. You should answer "Yes" or "No". You should answer "Yes" in the following situations: All situations where the tutor asks or tells the student to do something actively or asks a question. If the Tutor asks practice questions. If the Tutor asks follow up questions. If the Tutor tells the Student to try something by themselves. If the Tutor asks the Student to explain their reasoning. If the Tutor asks the Student to show their work. If the Tutor asks the Student to recheck their answer. If the Tutor asks the Student to talk through their answer. If the Tutor asks the student whether they would like to learn more. If the Tutor asks whether the student understood. Answer "No" in the following situations: If the Tutor does not ask the Student to do anything actively and also not asks a question. If the Tutor simply comments on the Student's answer like "good job" or "so close" or "that is incorrect" without actively asking the student to do something. If the Tutor explains or states a concept or an answer without asking the student to do something.'''
rubric2_prompt_basic = '''You are a Critic giving feedback on the Tutor's Tutoring skills. The Tutor should always promote active engagement. The Tutor can promote active engagement from the Student by asking follow-up questions to dig deeper, asking whether the Student would like to learn more, asking the Student to try something for themselves, and providing practice problems. For the given conversation, your task is to determine if the Tutor promotes active engagement at their specific point of progress in the conversation. You should answer only "Yes" or "No".'''

rubric4_prompt = '''You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor has a positive tone at their last utterance. The Tutor must be highly positive, enthusiastic and encouraging in their use of language. For each conversation, only answer "Yes" or "No". Answer "Yes" if: The Tutor is explicitly using highly positive, enthusiastic and encouraging and motivating language. Tutor uses positive expressions like "great try!", "you're almost there!". Answer "No" if: The Tutor has a neutral tone. The Tutor is somewhat positive. The Tutor is asking questions or making suggestions for the student, without using explicit positive language. Tutor uses only somewhat positive expressions like "that works." or "good try". Note that you should not imply the positivity of the Tutor's tone from the given text. Judge only based on the explicitly chosen words, expressions and punctuation marks.'''
rubric4_prompt_basic = '''You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor has a positive tone at their specific point of progress in the conversation. For each conversation, only answer „Yes" or „No". Answer „Yes" if the Tutor is highly positive, enthusiastic and encouraging. Answer „No“  if the Tutor is neutral or somewhat positive.'''

rubric5_prompt = '''You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor point out the Student's mistake at their last utterance. You may assume that the student's answer contains an error. You can always assume that the Tutor knows the correct answer. You should answer only „Yes“ or „No“. Answer „Yes“ in the following situations: The Tutor points out the mistake or opportunities for improvement. The Tutor identifies and addresses the Student's misconceptions. The Tutor asks a question which draws attention to the mistake. The Tutor points out the Student's error through a practice question or an example. Answer „No“ in the following situations: The Tutor states that the Student's statement is right even though it is not. The Tutor does not point out the mistake directly or not at all. The Tutor gives the right answer without pointing out what was wrong. The Tutor states that the Student's statement is wrong without pointing out what was wrong.'''
rubric5_prompt_basic = '''You are a Critic giving feedback on the Tutor's Tutoring skills. For the given conversation, your task is to determine if the Tutor point out the Student's mistake at their specific point of progress in the conversation. You may assume that the student's answer contains an error. You can always assume that the Tutor knows the correct answer. You should answer only „Yes“ or „No“. Answer „Yes“ in the following situations: The Tutor points out the mistake or opportunities for improvement. The Tutor identifies and addresses the Student's misconceptions. The Tutor asks a question which draws attention to the mistake. Answer „No“ in the following situations: The Tutor states that the Student's statement is right even though it is not. The Tutor does not point out the mistake directly or not at all. The Tutor gives the right answer without pointing out what was wrong. The Tutor states that the Student's statement is wrong without pointing out what was wrong.'''

with open('batchinput_2.jsonl', 'w') as json_file:

    for index, row in data.iterrows():

        requests = [

        {"custom_id": f"request{index}_1_1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", "messages": [{"role": "system", "content": rubric1_prompt},{"role": "user", "content": row['text']}],"temperature": 0, "max_tokens": 1000}}
        ,{"custom_id": f"request{index}_1_2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", 
                                                                                                        "messages": [
                                                                                                            {"role": "system", "content": rubric1_prompt},
                                                                                                            {"role":"user", "content": example_1}, 
                                                                                                            {"role": "assistant", "content": "No"}, 
                                                                                                            {"role": "user", "content": example_2}, 
                                                                                                            {"role": "assistant", "content": "Yes"},
                                                                                                            {"role": "user", "content": row['text']}
                                                                                                                    ] ,"temperature": 0, "max_tokens": 1000}}
        ,{"custom_id": f"request{index}_1_3", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", "messages": [{"role": "system", "content": rubric1_prompt_basic},{"role": "user", "content": row['text']}],"temperature": 0, "max_tokens": 1000}}
        ,{"custom_id": f"request{index}_1_4", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", 
                                                                                                       "messages": [
                                                                                                            {"role": "system", "content": rubric1_prompt_basic},
                                                                                                            {"role":"user", "content": example_1}, 
                                                                                                            {"role": "assistant", "content": "No"}, 
                                                                                                            {"role": "user", "content": example_2}, 
                                                                                                            {"role": "assistant", "content": "Yes"},
                                                                                                            {"role": "user", "content": row['text']}
                                                                                                                    ],"temperature": 0, "max_tokens": 1000}}
        
        ,{"custom_id": f"request{index}_2_1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", "messages": [{"role": "system", "content": rubric2_prompt},{"role": "user", "content": row['text']}],"temperature": 0, "max_tokens": 1000}}
        ,{"custom_id": f"request{index}_2_2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o",
                                                                                                       "messages": [
                                                                                                            {"role": "system", "content": rubric2_prompt},
                                                                                                            {"role":"user", "content": example_1}, 
                                                                                                            {"role": "assistant", "content": "Yes"}, 
                                                                                                            {"role": "user", "content": example_2}, 
                                                                                                            {"role": "assistant", "content": "No"},
                                                                                                            {"role": "user", "content": row['text']}
                                                                                                                    ],"temperature": 0,"max_tokens": 1000}}
        ,{"custom_id": f"request{index}_2_3", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", "messages": [{"role": "system", "content": rubric2_prompt_basic},{"role": "user", "content": row['text']}],"temperature": 0, "max_tokens": 1000}}
        ,{"custom_id": f"request{index}_2_4", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", 
                                                                                                       "messages": [
                                                                                                            {"role": "system", "content": rubric2_prompt_basic},
                                                                                                            {"role":"user", "content": example_1}, 
                                                                                                            {"role": "assistant", "content": "Yes"}, 
                                                                                                            {"role": "user", "content": example_2}, 
                                                                                                            {"role": "assistant", "content": "No"},
                                                                                                            {"role": "user", "content": row['text']}
                                                                                                                    ],"temperature": 0, "max_tokens": 1000}}
         
        ,{"custom_id": f"request{index}_4_1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", "messages": [{"role": "system", "content": rubric4_prompt},{"role": "user", "content": row['text']}],"temperature": 0, "max_tokens": 1000}}
        ,{"custom_id": f"request{index}_4_2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", 
                                                                                                       "messages": [
                                                                                                            {"role": "system", "content": rubric4_prompt},
                                                                                                            {"role":"user", "content": example_1}, 
                                                                                                            {"role": "assistant", "content": "No"}, 
                                                                                                            {"role": "user", "content": example_2}, 
                                                                                                            {"role": "assistant", "content": "Yes"},
                                                                                                            {"role": "user", "content": row['text']}
                                                                                                                    ],"temperature": 0, "max_tokens": 1000}}
        ,{"custom_id": f"request{index}_4_3", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", "messages": [{"role": "system", "content": rubric4_prompt_basic},{"role": "user", "content": row['text']}],"temperature": 0, "max_tokens": 1000}}
        ,{"custom_id": f"request{index}_4_4", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", 
                                                                                                       "messages": [
                                                                                                            {"role": "system", "content": rubric4_prompt_basic},
                                                                                                            {"role":"user", "content": example_1}, 
                                                                                                            {"role": "assistant", "content": "No"}, 
                                                                                                            {"role": "user", "content": example_2}, 
                                                                                                            {"role": "assistant", "content": "Yes"},
                                                                                                            {"role": "user", "content": row['text']}
                                                                                                                   ],"temperature": 0, "max_tokens": 1000}}

        ,{"custom_id": f"request{index}_5_1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", "messages": [{"role": "system", "content": rubric5_prompt},{"role": "user", "content": row['text']}],"temperature": 0, "max_tokens": 1000}}
        ,{"custom_id": f"request{index}_5_2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", 
                                                                                                       "messages": [
                                                                                                            {"role": "system", "content": rubric5_prompt},
                                                                                                            {"role":"user", "content": example_1}, 
                                                                                                            {"role": "assistant", "content": "No"}, 
                                                                                                            {"role": "user", "content": example_2}, 
                                                                                                            {"role": "assistant", "content": "Yes"},
                                                                                                            {"role": "user", "content": row['text']}
                                                                                                                  ],"temperature": 0, "max_tokens": 1000}}
        ,{"custom_id": f"request{index}_5_3", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", "messages": [{"role": "system", "content": rubric5_prompt_basic},{"role": "user", "content": row['text']}],"temperature": 0, "max_tokens": 1000}}
        ,{"custom_id": f"request{index}_5_4", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-4o", 
                                                                                                       "messages": [
                                                                                                            {"role": "system", "content": rubric5_prompt_basic},
                                                                                                            {"role":"user", "content": example_1}, 
                                                                                                            {"role": "assistant", "content": "No"}, 
                                                                                                            {"role": "user", "content": example_2}, 
                                                                                                            {"role": "assistant", "content": "Yes"},
                                                                                                            {"role": "user", "content": row['text']}
                                                                                                                  ],"temperature": 0, "max_tokens": 1000}}
        
        ]

        if pd.isna(row['rubric_1']):
            requests = [req for req in requests if not req['custom_id'].startswith(f"request{index}_1")]
        
        if pd.isna(row['rubric_2']):
            requests = [req for req in requests if not req['custom_id'].startswith(f"request{index}_2")]
        
        if pd.isna(row['rubric_4']):
            requests = [req for req in requests if not req['custom_id'].startswith(f"request{index}_4")]

        if pd.isna(row['rubric_5']):
            requests = [req for req in requests if not req['custom_id'].startswith(f"request{index}_5")]
   

        for req in requests:
            json_file.write(json.dumps(req) + '\n')

  


