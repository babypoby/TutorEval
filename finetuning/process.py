import pandas as pd

data = pd.read_csv('data_combined.csv')
#only columns conversation id, text and rubric
data = data[['conversation_id', 'text', 'rubric_4']]
#drop rows with missing values
data = data.dropna()
print(len(data))
# Exclude rows where 'conversation_id' is in test_set_ids.txt where each id is in a new line
test_set = pd.read_csv('test_set_ids.txt', header=None)
test_set.columns = ['conversation_id']
print(len(test_set))

truth_not_test = data[~data['conversation_id'].isin(test_set['conversation_id'])]
print("hi")
print(len(truth_not_test))
#change name of column rubric 4 to response
truth_not_test = truth_not_test.rename(columns = {'rubric_4':'response'})

#test whether text_data_all_with_responses_new.csv already contains rows with conversation_id in truth_not_test
text_data_all_with_responses_new = pd.read_csv('text_data_all_with_responses_new.csv') 
if len(text_data_all_with_responses_new[text_data_all_with_responses_new['conversation_id'].isin(truth_not_test['conversation_id'])]) > 0:
    print("text_data_all_with_responses_new.csv already contains rows with conversation_id in truth_not_test")


#combine truth_not_test with text_data_all_with_responses_new
truth_not_test = pd.concat([truth_not_test, text_data_all_with_responses_new])

print(len(truth_not_test))
print(truth_not_test.head())
#save to csv   
truth_not_test.to_csv('bigdatachunk.csv', index=False)

#test if truth_not_test contains conversation_id in test_set_ids.txt
if len(truth_not_test[truth_not_test['conversation_id'].isin(test_set['conversation_id'])]) > 0:
    print("truth_not_test contains conversation_id in test_set_ids.txt")