import json
import pandas as pd
import re

def extract_number(string):
    # Define a regular expression pattern to capture the number after "request"
    pattern = re.compile(r'request(\d+)_')
    
    # Use the pattern to search the string
    match = pattern.search(string)
    
    if match:
        # Extract the captured group, which is the number after "request"
        number = match.group(1)
        return int(number)  # Convert to integer if needed
    else:
        # Return None or handle the case if the pattern doesn't match
        return None

# Open the file in read mode
data = pd.read_csv('data_combined.csv')

rubric1_ex = 0
rubric1_ex_yn = 0
rubric1_ex_ny = 0
rubric1_ex_nn = 0

rubric1_nex = 0
rubric1_nex_yy = 0
rubric1_nex_yn = 0
rubric1_nex_ny = 0
rubric1_nex_nn = 0

rubric1_bas_ex = 0
rubric1_bas_ex_yy = 0
rubric1_bas_ex_yn = 0
rubric1_bas_ex_ny = 0
rubric1_bas_ex_nn = 0

rubric1_bas_nex = 0
rubric1_bas_nex_yy = 0
rubric1_bas_nex_yn = 0
rubric1_bas_nex_ny = 0
rubric1_bas_nex_nn = 0

rubric2_ex = 0
rubric2_ex_yy = 0
rubric2_ex_yn = 0
rubric2_ex_ny = 0
rubric2_ex_nn = 0

rubric2_nex = 0
rubric2_nex_yy = 0
rubric2_nex_yn = 0
rubric2_nex_ny = 0
rubric2_nex_nn = 0

rubric2_bas_ex = 0
rubric2_bas_ex_yy = 0
rubric2_bas_ex_yn = 0
rubric2_bas_ex_ny = 0
rubric2_bas_ex_nn = 0

rubric2_bas_nex = 0
rubric2_bas_nex_yy = 0
rubric2_bas_nex_yn = 0
rubric2_bas_nex_ny = 0
rubric2_bas_nex_nn = 0

rubric4_ex = 0
rubric4_ex_yy = 0
rubric4_ex_yn = 0
rubric4_ex_ny = 0
rubric4_ex_nn = 0

rubric4_nex = 0
rubric4_nex_yy = 0
rubric4_nex_yn = 0
rubric4_nex_ny = 0
rubric4_nex_nn = 0

rubric4_bas_ex = 0
rubric4_bas_ex_yy = 0
rubric4_bas_ex_yn = 0
rubric4_bas_ex_ny = 0
rubric4_bas_ex_nn = 0

rubric4_bas_nex = 0
rubric4_bas_nex_yy = 0
rubric4_bas_nex_yn = 0
rubric4_bas_nex_ny = 0
rubric4_bas_nex_nn = 0

rubric5_ex = 0
rubric5_ex_yy = 0
rubric5_ex_yn = 0
rubric5_ex_ny = 0
rubric5_ex_nn = 0

rubric5_nex = 0
rubric5_nex_yy = 0
rubric5_nex_yn = 0
rubric5_nex_ny = 0
rubric5_nex_nn = 0

rubric5_bas_ex = 0
rubric5_bas_ex_yy = 0
rubric5_bas_ex_yn = 0
rubric5_bas_ex_ny = 0
rubric5_bas_ex_nn = 0

rubric5_bas_nex = 0
rubric5_bas_nex_yy = 0
rubric5_bas_nex_yn = 0
rubric5_bas_nex_ny = 0
rubric5_bas_nex_nn = 0

with open('output_temp0.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Strip any leading/trailing whitespace (including newlines)
        line = line.strip()
        if line:  # Ensure the line is not empty
            # Parse the JSON object from the line
            json_object = json.loads(line)
            index = extract_number(json_object['custom_id'])

            if json_object['custom_id'].startswith(f"request{index}_1"):

                rubric1 = data.iloc[index]['rubric_1']

                if rubric1 != json_object['response']['body']['choices'][0]['message']['content']:

                    if json_object['custom_id'] == f"request{index}_1_1":
                        rubric1_nex += 1
                        if (rubric1 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric1_nex_yy += 1
                        if (rubric1 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric1_nex_yn += 1
                        if (rubric1 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric1_nex_ny += 1
                        if (rubric1 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric1_nex_nn += 1

                    if json_object['custom_id'] == f"request{index}_1_2":
                        rubric1_ex += 1
                        if (rubric1 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric1_ex_yy += 1
                        if (rubric1 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric1_ex_yn += 1
                        if (rubric1 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric1_ex_ny += 1
                        if (rubric1 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric1_ex_nn += 1

                    if json_object['custom_id'] == f"request{index}_1_3":
                        rubric1_bas_nex += 1
                        if (rubric1 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric1_bas_nex_yy += 1
                        if (rubric1 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric1_bas_nex_yn += 1
                        if (rubric1 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric1_bas_nex_ny += 1
                        if (rubric1 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric1_bas_nex_nn += 1
                
                    if json_object['custom_id'] == f"request{index}_1_4":
                        rubric1_bas_ex += 1
                        if (rubric1 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric1_bas_ex_yy += 1
                        if (rubric1 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric1_bas_ex_yn += 1
                        if (rubric1 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric1_bas_ex_ny += 1
                        if (rubric1 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric1_bas_ex_nn += 1
            
            if json_object['custom_id'].startswith(f"request{index}_2"):
                rubric2 = data.iloc[index]['rubric_2']
                if rubric2 != json_object['response']['body']['choices'][0]['message']['content']:
                    if json_object['custom_id'] == f"request{index}_2_1":
                        rubric2_nex += 1
                        if (rubric2 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric2_nex_yy += 1
                        if (rubric2 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric2_nex_yn += 1
                        if (rubric2 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric2_nex_ny += 1
                        if (rubric2 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric2_nex_nn += 1
                
                    if json_object['custom_id'] == f"request{index}_2_2":
                        rubric2_ex += 1
                        if (rubric2 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric2_ex_yy += 1
                        if (rubric2 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric2_ex_yn += 1
                        if (rubric2 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric2_ex_ny += 1
                        if (rubric2 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric2_ex_nn += 1

                    if json_object['custom_id'] == f"request{index}_2_3":
                        rubric2_bas_nex += 1
                        if (rubric2 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric2_bas_nex_yy += 1
                        if (rubric2 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric2_bas_nex_yn += 1
                        if (rubric2 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric2_bas_nex_ny += 1
                        if (rubric2 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric2_bas_nex_nn += 1

                    if json_object['custom_id'] == f"request{index}_2_4":
                        rubric2_bas_ex += 1
                        if (rubric2 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric2_bas_ex_yy += 1
                        if (rubric2 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric2_bas_ex_yn += 1
                        if (rubric2 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric2_bas_ex_ny += 1
                        if (rubric2 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric2_bas_ex_nn += 1
            
            if json_object['custom_id'].startswith(f"request{index}_4"):
                rubric4 = data.iloc[index]['rubric_4']
                if rubric4 != json_object['response']['body']['choices'][0]['message']['content']:
                    if json_object['custom_id'] == f"request{index}_4_1":
                        rubric4_nex += 1
                        if (rubric4 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric4_nex_yy += 1
                        if (rubric4 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric4_nex_yn += 1
                        if (rubric4 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric4_nex_ny += 1
                        if (rubric4 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric4_nex_nn += 1
                    
                    if json_object['custom_id'] == f"request{index}_4_2":
                        rubric4_ex += 1
                        if (rubric4 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric4_ex_yy += 1
                        if (rubric4 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric4_ex_yn += 1
                        if (rubric4 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric4_ex_ny += 1
                        if (rubric4 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric4_ex_nn += 1

                    if json_object['custom_id'] == f"request{index}_4_3":
                        rubric4_bas_nex += 1
                        if (rubric4 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric4_bas_nex_yy += 1
                        if (rubric4 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric4_bas_nex_yn += 1
                        if (rubric4 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric4_bas_nex_ny += 1
                        if (rubric4 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric4_bas_nex_nn += 1

                    if json_object['custom_id'] == f"request{index}_4_4":
                        rubric4_bas_ex += 1
                        if (rubric4 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric4_bas_ex_yy += 1
                        if (rubric4 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric4_bas_ex_yn += 1
                        if (rubric4 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric4_bas_ex_ny += 1
                        if (rubric4 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric4_bas_ex_nn += 1
            
            if json_object['custom_id'].startswith(f"request{index}_5"):
                rubric5 = data.iloc[index]['rubric_5']
                if rubric5 != json_object['response']['body']['choices'][0]['message']['content']:
                    if json_object['custom_id'] == f"request{index}_5_1":
                        rubric5_nex += 1
                        if (rubric5 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric5_nex_yy += 1
                        if (rubric5 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric5_nex_yn += 1
                        if (rubric5 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric5_nex_ny += 1
                        if (rubric5 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric5_nex_nn += 1

                    if json_object['custom_id'] == f"request{index}_5_2":
                        rubric5_ex += 1
                        if (rubric5 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric5_ex_yy += 1
                        if (rubric5 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric5_ex_yn += 1
                        if (rubric5 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric5_ex_ny += 1
                        if (rubric5 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric5_ex_nn += 1

                    if json_object['custom_id'] == f"request{index}_5_3":
                        rubric5_bas_nex += 1
                        if (rubric5 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric5_bas_nex_yy += 1
                        if (rubric5 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric5_bas_nex_yn += 1
                        if (rubric5 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric5_bas_nex_ny += 1
                        if (rubric5 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric5_bas_nex_nn += 1

                    if json_object['custom_id'] == f"request{index}_5_4":
                        rubric5_bas_ex += 1
                        if (rubric5 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric5_bas_ex_yy += 1
                        if (rubric5 == "Yes") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric5_bas_ex_yn += 1
                        if (rubric5 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "Yes"):
                            rubric5_bas_ex_ny += 1
                        if (rubric5 == "No") and (json_object['response']['body']['choices'][0]['message']['content'] == "No"):
                            rubric5_bas_ex_nn += 1

print(f"Number of wrong answers for rubric 1, no examples, prompt: {rubric1_nex}")
print(f"Number of wrong answers for rubric 1, no examples, prompt, yes-yes: {rubric1_nex_yy}")
print(f"Number of wrong answers for rubric 1, no examples, prompt, yes-no: {rubric1_nex_yn}")
print(f"Number of wrong answers for rubric 1, no examples, prompt, no-yes: {rubric1_nex_ny}")
print(f"Number of wrong answers for rubric 1, no examples, prompt, no-no: {rubric1_nex_nn}")

print(f"Number of wrong answers for rubric 1, examples, prompt: {rubric1_ex}")
print(f"Number of wrong answers for rubric 1, examples, prompt, yes-yes: {rubric1_ex_yy}")
print(f"Number of wrong answers for rubric 1, examples, prompt, yes-no: {rubric1_ex_yn}")
print(f"Number of wrong answers for rubric 1, examples, prompt, no-yes: {rubric1_ex_ny}")
print(f"Number of wrong answers for rubric 1, examples, prompt, no-no: {rubric1_ex_nn}")

print(f"Number of wrong answers for rubric 1, no examples, basic prompt: {rubric1_bas_nex}")
print(f"Number of wrong answers for rubric 1, no examples, basic prompt, yes-yes: {rubric1_bas_nex_yy}")
print(f"Number of wrong answers for rubric 1, no examples, basic prompt, yes-no: {rubric1_bas_nex_yn}")
print(f"Number of wrong answers for rubric 1, no examples, basic prompt, no-yes: {rubric1_bas_nex_ny}")
print(f"Number of wrong answers for rubric 1, no examples, basic prompt, no-no: {rubric1_bas_nex_nn}")

print(f"Number of wrong answers for rubric 1, examples, basic prompt: {rubric1_bas_ex}")
print(f"Number of wrong answers for rubric 1, examples, basic prompt, yes-yes: {rubric1_bas_ex_yy}")
print(f"Number of wrong answers for rubric 1, examples, basic prompt, yes-no: {rubric1_bas_ex_yn}")
print(f"Number of wrong answers for rubric 1, examples, basic prompt, no-yes: {rubric1_bas_ex_ny}")
print(f"Number of wrong answers for rubric 1, examples, basic prompt, no-no: {rubric1_bas_ex_nn}")

print(f"Number of wrong answers for rubric 2, no examples, prompt: {rubric2_nex}") 
print(f"Number of wrong answers for rubric 2, no examples, prompt, yes-yes: {rubric2_nex_yy}")
print(f"Number of wrong answers for rubric 2, no examples, prompt, yes-no: {rubric2_nex_yn}")
print(f"Number of wrong answers for rubric 2, no examples, prompt, no-yes: {rubric2_nex_ny}")
print(f"Number of wrong answers for rubric 2, no examples, prompt, no-no: {rubric2_nex_nn}")

print(f"Number of wrong answers for rubric 2, examples, prompt: {rubric2_ex}")
print(f"Number of wrong answers for rubric 2, examples, prompt, yes-yes: {rubric2_ex_yy}")
print(f"Number of wrong answers for rubric 2, examples, prompt, yes-no: {rubric2_ex_yn}")
print(f"Number of wrong answers for rubric 2, examples, prompt, no-yes: {rubric2_ex_ny}")
print(f"Number of wrong answers for rubric 2, examples, prompt, no-no: {rubric2_ex_nn}")

print(f"Number of wrong answers for rubric 2, no examples, basic prompt: {rubric2_bas_nex}")
print(f"Number of wrong answers for rubric 2, no examples, basic prompt, yes-yes: {rubric2_bas_nex_yy}")
print(f"Number of wrong answers for rubric 2, no examples, basic prompt, yes-no: {rubric2_bas_nex_yn}")
print(f"Number of wrong answers for rubric 2, no examples, basic prompt, no-yes: {rubric2_bas_nex_ny}")
print(f"Number of wrong answers for rubric 2, no examples, basic prompt, no-no: {rubric2_bas_nex_nn}")

print(f"Number of wrong answers for rubric 2, examples, basic prompt: {rubric2_bas_ex}")
print(f"Number of wrong answers for rubric 2, examples, basic prompt, yes-yes: {rubric2_bas_ex_yy}")
print(f"Number of wrong answers for rubric 2, examples, basic prompt, yes-no: {rubric2_bas_ex_yn}")
print(f"Number of wrong answers for rubric 2, examples, basic prompt, no-yes: {rubric2_bas_ex_ny}")
print(f"Number of wrong answers for rubric 2, examples, basic prompt, no-no: {rubric2_bas_ex_nn}")

print(f"Number of wrong answers for rubric 4, no examples, prompt: {rubric4_nex}")
print(f"Number of wrong answers for rubric 4, no examples, prompt, yes-yes: {rubric4_nex_yy}")
print(f"Number of wrong answers for rubric 4, no examples, prompt, yes-no: {rubric4_nex_yn}")
print(f"Number of wrong answers for rubric 4, no examples, prompt, no-yes: {rubric4_nex_ny}")
print(f"Number of wrong answers for rubric 4, no examples, prompt, no-no: {rubric4_nex_nn}")

print(f"Number of wrong answers for rubric 4, examples, prompt: {rubric4_ex}")
print(f"Number of wrong answers for rubric 4, examples, prompt, yes-yes: {rubric4_ex_yy}")
print(f"Number of wrong answers for rubric 4, examples, prompt, yes-no: {rubric4_ex_yn}")
print(f"Number of wrong answers for rubric 4, examples, prompt, no-yes: {rubric4_ex_ny}")
print(f"Number of wrong answers for rubric 4, examples, prompt, no-no: {rubric4_ex_nn}")

print(f"Number of wrong answers for rubric 4, no examples, basic prompt: {rubric4_bas_nex}")
print(f"Number of wrong answers for rubric 4, no examples, basic prompt, yes-yes: {rubric4_bas_nex_yy}")
print(f"Number of wrong answers for rubric 4, no examples, basic prompt, yes-no: {rubric4_bas_nex_yn}")
print(f"Number of wrong answers for rubric 4, no examples, basic prompt, no-yes: {rubric4_bas_nex_ny}")
print(f"Number of wrong answers for rubric 4, no examples, basic prompt, no-no: {rubric4_bas_nex_nn}")

print(f"Number of wrong answers for rubric 4, examples, basic prompt: {rubric4_bas_ex}")
print(f"Number of wrong answers for rubric 4, examples, basic prompt, yes-yes: {rubric4_bas_ex_yy}")
print(f"Number of wrong answers for rubric 4, examples, basic prompt, yes-no: {rubric4_bas_ex_yn}")
print(f"Number of wrong answers for rubric 4, examples, basic prompt, no-yes: {rubric4_bas_ex_ny}")
print(f"Number of wrong answers for rubric 4, examples, basic prompt, no-no: {rubric4_bas_ex_nn}")

print(f"Number of wrong answers for rubric 5, no examples, prompt: {rubric5_nex}")
print(f"Number of wrong answers for rubric 5, no examples, prompt, yes-yes: {rubric5_nex_yy}")
print(f"Number of wrong answers for rubric 5, no examples, prompt, yes-no: {rubric5_nex_yn}")
print(f"Number of wrong answers for rubric 5, no examples, prompt, no-yes: {rubric5_nex_ny}")
print(f"Number of wrong answers for rubric 5, no examples, prompt, no-no: {rubric5_nex_nn}")

print(f"Number of wrong answers for rubric 5, examples, prompt: {rubric5_ex}")
print(f"Number of wrong answers for rubric 5, examples, prompt, yes-yes: {rubric5_ex_yy}")
print(f"Number of wrong answers for rubric 5, examples, prompt, yes-no: {rubric5_ex_yn}")
print(f"Number of wrong answers for rubric 5, examples, prompt, no-yes: {rubric5_ex_ny}")
print(f"Number of wrong answers for rubric 5, examples, prompt, no-no: {rubric5_ex_nn}")

print(f"Number of wrong answers for rubric 5, no examples, basic prompt: {rubric5_bas_nex}")
print(f"Number of wrong answers for rubric 5, no examples, basic prompt, yes-yes: {rubric5_bas_nex_yy}")
print(f"Number of wrong answers for rubric 5, no examples, basic prompt, yes-no: {rubric5_bas_nex_yn}")
print(f"Number of wrong answers for rubric 5, no examples, basic prompt, no-yes: {rubric5_bas_nex_ny}")
print(f"Number of wrong answers for rubric 5, no examples, basic prompt, no-no: {rubric5_bas_nex_nn}")

print(f"Number of wrong answers for rubric 5, examples, basic prompt: {rubric5_bas_ex}")
print(f"Number of wrong answers for rubric 5, examples, basic prompt, yes-yes: {rubric5_bas_ex_yy}")
print(f"Number of wrong answers for rubric 5, examples, basic prompt, yes-no: {rubric5_bas_ex_yn}")
print(f"Number of wrong answers for rubric 5, examples, basic prompt, no-yes: {rubric5_bas_ex_ny}")
print(f"Number of wrong answers for rubric 5, examples, basic prompt, no-no: {rubric5_bas_ex_nn}")
