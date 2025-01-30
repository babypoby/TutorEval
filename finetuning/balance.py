import pandas as pd

# Load ground truth data
data_r4 = pd.read_csv('data_combined.csv')
#only columns conversation id, text and rubric
data_r4 = data_r4[['conversation_id', 'text', 'rubric_4']]
#drop rows with missing values
data_r4 = data_r4.dropna()

yes = 0
no = 0

for (index,row) in data_r4.iterrows():
    if row['rubric_4'] == 'Yes':
        yes += 1
    else:
        no += 1

text_data_all_with_responses_new = pd.read_csv('text_data_all_with_responses_new.csv') 

yes_new = 0
no_new = 0

for (index,row) in text_data_all_with_responses_new.iterrows():
    if row['response'] == 'Yes':
        yes_new += 1
    else:
        no_new += 1


print(f"yes: {yes}")
print(f"no: {no}")
print(f"yes_new: {yes_new}")
print(f"no_new: {no_new}")
