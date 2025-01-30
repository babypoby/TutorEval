import pandas as pd
data = pd.read_csv('data_combined.csv')

rubric1_yes = 0
rubric2_yes = 0
rubric4_yes = 0
rubric5_yes = 0

rubric1_no = 0
rubric2_no = 0
rubric4_no = 0
rubric5_no = 0

for i in range(0, len(data)):

    rubric1 = data.iloc[i]['rubric_1']
    rubric2 = data.iloc[i]['rubric_2']
    rubric4 = data.iloc[i]['rubric_4']
    rubric5 = data.iloc[i]['rubric_5']

    print(rubric1, rubric2, rubric4, rubric5)
    
    if rubric1 == "Yes":
        rubric1_yes += 1
    elif rubric1 == "No":
        rubric1_no += 1
    
    if rubric2 == "Yes":
        rubric2_yes += 1
    elif rubric2 == "No":
        rubric2_no += 1
    
    if rubric4 == "Yes":
        rubric4_yes += 1
    elif rubric4 == "No":
        rubric4_no += 1
    
    if rubric5 == "Yes":
        rubric5_yes += 1
    elif rubric5 == "No":
        rubric5_no += 1

print("Rubric 1 Yes: ", rubric1_yes)
print("Rubric 1 No: ", rubric1_no)
print("Rubric 2 Yes: ", rubric2_yes)
print("Rubric 2 No: ", rubric2_no)
print("Rubric 4 Yes: ", rubric4_yes)
print("Rubric 4 No: ", rubric4_no)
print("Rubric 5 Yes: ", rubric5_yes)
print("Rubric 5 No: ", rubric5_no)

