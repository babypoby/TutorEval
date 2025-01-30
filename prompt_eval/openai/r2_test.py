import pandas as pd
import json
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

print ('Total:', len(data))
print('Bridge 1:', len(bridge_1))
print('Bridge 2:', len(bridge_2))
print('Mathdial:', len(mathdial))

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


with open('output_temp0.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Strip any leading/trailing whitespace (including newlines)
        line = line.strip()
        if line:  # Ensure the line is not empty
            # Parse the JSON object from the line
            json_object = json.loads(line)
            index = extract_number(json_object['custom_id'])

            if json_object['custom_id'].startswith(f"request{index}_5_2"):

                rubric2 = data.iloc[index]['rubric_5']
                response = json_object['response']['body']['choices'][0]['message']['content']

                if index in bridge_1:
                    if response == 'Yes':
                        bridge_1_yes += 1
                    elif response == 'No':
                        bridge_1_no += 1
                    if rubric2 == 'Yes':
                        bridge_1_org_yes += 1
                    elif rubric2 == 'No':
                        bridge_1_org_no += 1
                    
                elif index in bridge_2:
                    if response == 'Yes':
                        bridge_2_yes += 1
                    elif response == 'No':
                        bridge_2_no += 1
                    if rubric2 == 'Yes':
                        bridge_2_org_yes += 1
                    elif rubric2 == 'No':
                        bridge_2_org_no += 1

                elif index in mathdial:
                    if response == 'Yes':
                        mathdial_yes += 1
                    elif response == 'No':
                        mathdial_no += 1
                    if rubric2 == 'Yes':
                        mathdial_org_yes += 1
                    elif rubric2 == 'No':
                        mathdial_org_no += 1

            

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