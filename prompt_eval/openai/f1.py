def calculate_f1_score(tp, fp, fn):
    """
    Calculate the F1 score given true positives (TP), false positives (FP), and false negatives (FN).

    Parameters:
        tp (int): True Positives
        fp (int): False Positives
        fn (int): False Negatives

    Returns:
        float: The F1 score, or 0 if TP, FP, and FN are all zero.
    """
    if tp == 0 and fp == 0 and fn == 0:
        return 0.0  # Handle edge case where no predictions or true positives exist
    
    # Precision calculation
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    
    # Recall calculation
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    
    # F1 score calculation
    if precision + recall == 0:
        return 0.0  # Avoid division by zero
    f1_score = 2 * (precision * recall) / (precision + recall)

    return f1_score

def generate_latex_table(matrix, row_names, col_names, rubric_name):
    """
    Generate LaTeX code for a table with special handling for matrix values greater than 1.

    Parameters:
        matrix (list of list of floats): 2D matrix where each entry is a float value
        row_names (list of str): Row labels
        col_names (list of str): Column labels
        rubric_name (str): Name of the rubric

    Returns:
        str: LaTeX table code as a string
    """
    # Column headers
    col_header = " & ".join(col_names) + " \\\\\n\\hline\n"
    
    # Begin table
    table_header = (
        "\\begin{table}\n"
        "\\begin{center}\n"
        "\\begin{tabular}{ |>{\\centering\\arraybackslash}m{2.5cm}|" +
        "|".join([f">{{\\centering\\arraybackslash}}m{{3cm}}" for _ in col_names]) +
        "| }\n"
        "\\hline\n"
        " & " + col_header
    )
    
    # Table body
    table_body = ""
    for row_name, row in zip(row_names, matrix):
        table_body += f"{row_name} "
        for value in row:
            if value >= 1:
                table_body += f"& NaN, {value} "
            else:
                table_body += f"& {value:.3f} "
        table_body += "\\\\\n\\hline\n"
    
    # End table
    table_footer = (
        "\\end{tabular}\n"
        "\\end{center}\n"
        f"\\caption{{Error rate of Models for Rubric \"{rubric_name}\"}}\n"
        "\\label{{tab:error_rate_rubric}}\n"
        "\\end{table}"
    )
    
    return table_header + table_body + table_footer


rubric1_total = 22
rubric2_total = 162
rubric4_total = 65
rubric5_total = 106

# 1b d fp , 1b d fn, 1b s fp, 1b s fn, 1b d nex fp, 1b d nex fn, 1b s nex fp, 1b s nex fn
rubric1_1 = [3,22,4,22,15,22,36,15]
# number of wrong answers: 25,26,40,54
n1_1_1 = 25
n1_1_2 = 26
n1_1_3 = 40
n1_1_4 = 54

rubric1_2 = [52,12,147,3,63,7,95,5]
# number of wrong answers: 64,150,70,100
n1_2_1 = 64
n1_2_2 = 150
n1_2_3 = 70
n1_2_4 = 100

rubric1_3 = [22,10,110,2,112,1,181,0]
# number of wrong answers: 32,112,113,181
n1_3_1 = 32
n1_3_2 = 112
n1_3_3 = 113
n1_3_4 = 181

rubric1_4 = [7,6,20,6,3,9,6,9]
# number of wrong answers: 13,26,12,15
n1_4_1 = 13
n1_4_2 = 26
n1_4_3 = 12
n1_4_4 = 15

rubric1_5 = [4,7,15,6,3,7,10,8]
# number of wrong answers: 11,21,10,18
n1_5_1 = 11
n1_5_2 = 21
n1_5_3 = 10
n1_5_4 = 18


rubric1_6 = [3,7,7,5,5,7,19,2]
# number of wrong answers: 10,12,14,22
n1_6_1 = 10
n1_6_2 = 12
n1_6_3 = 14
n1_6_4 = 22

rubric1_7 = [7,5,8,4,14,4,15,3]
# number of wrong answers: 12,12,18,18
n1_7_1 = 12
n1_7_2 = 12
n1_7_3 = 18
n1_7_4 = 18


rubric2_1 =[9,147,17,139,5,9,25,4]
# number of wrong answers: 158,156,215,207
n2_1_1 = 158
n2_1_2 = 156
n2_1_3 = 215
n2_1_4 = 207


rubric2_2 = [16,77,12,101,0,14,0,1]
# number of wrong answers: 93,113,197,231
n2_2_1 = 93
n2_2_2 = 113
n2_2_3 = 197
n2_2_4 = 231

rubric2_3 = [11,13,2,0,2,1,0,0]
# number of wrong answers: 63,189,229,231
n2_3_1 = 63
n2_3_2 = 189
n2_3_3 = 229
n2_3_4 = 231

rubric2_4= [8,12,4,34,1,29,0,5]
# number of wrong answers: 21,43,39,209
n2_4_1 = 21
n2_4_2 = 43
n2_4_3 = 39
n2_4_4 = 209

rubric2_5 = [12,10,5,17,2,12,2,1]
# number of wrong answers: 24,39,28,195
n2_5_1 = 24
n2_5_2 = 39
n2_5_3 = 28
n2_5_4 = 195

rubric2_6 = [10,7,6,18,6,1,5,6]
n2_6_1 = 18
n2_6_2 = 29
n2_6_3 = 154
n2_6_4 = 207

rubric2_7 = [2,10,4,26,4,10,5,58]
# number of wrong answers: 12,30,18,63
n2_7_1 = 12
n2_7_2 = 30
n2_7_3 = 18
n2_7_4 = 63

rubric4_1 = [101,6,62,16,107,0,68,3]
n4_1_1 = 107
n4_1_2 = 78
n4_1_3 = 138
n4_1_4 = 144

rubric4_2 = [60,12,62,22,1,58,0,62]
n4_2_1 = 72
n4_2_2 = 84
n4_2_3 = 60
n4_2_4 = 63

rubric4_3 = [4,32,23,31,5,28,70,11]
n4_3_1 = 36
n4_3_2 = 54
n4_3_3 = 35
n4_3_4 = 83

rubric4_4 = [6,20,12,23,1,37,3,29]
n4_4_1 = 26
n4_4_2 = 35
n4_4_3 = 39
n4_4_4 = 36

rubric4_5 = [4,20,6,32,1,32,6,23]
n4_5_1 = 26
n4_5_2 = 38
n4_5_3 = 33
n4_5_4 = 29

rubric4_6 = [3,20,17,9,2,24,24,5]
n4_6_1 = 23
n4_6_2 = 26
n4_6_3 = 26
n4_6_4 = 31

rubric4_7 = [6,23,19,15,0,40,1,42]
n4_7_1 = 29
n4_7_2 = 34
n4_7_3 = 40
n4_7_4 = 43

rubric5_1 = [0,102,1,102,25,15,23,30]
n5_1_1 = 102
n5_1_2 = 103
n5_1_3 = 133    
n5_1_4 = 131

rubric5_2 = [16,49,20,44,3,74,3,80]
n5_2_1 = 65
n5_2_2 = 64
n5_2_3 = 77
n5_2_4 = 83

rubric5_3  = [24,16,22,23,27,15,17,30]
n5_3_1 = 40
n5_3_2 = 45
n5_3_3 = 46
n5_3_4 = 51

rubric5_4 = [12,40,10,48,3,46,2,58]
n5_4_1 = 52
n5_4_2 = 58
n5_4_3 = 65
n5_4_4 = 75

rubric5_5 = [15,35,10,41,11,32,6,52]
n5_5_1 = 50
n5_5_2 = 51
n5_5_3 = 46
n5_5_4 = 60

rubric5_6 = [11,36,10,47,21,11,19,22]
n5_6_1 = 47 
n5_6_2 = 57
n5_6_3 = 81
n5_6_4 = 92

rubric5_7 = [17,17,16,25,22,14,20,21]
n5_7_1 = 34
n5_7_2 = 41
n5_7_3 = 36
n5_7_4 = 41

rubric1 = [rubric1_1, rubric1_2, rubric1_3, rubric1_4, rubric1_5, rubric1_6, rubric1_7]
rubric2 = [rubric2_1, rubric2_2, rubric2_3, rubric2_4, rubric2_5, rubric2_6, rubric2_7]
rubric4 = [rubric4_1, rubric4_2, rubric4_3, rubric4_4, rubric4_5, rubric4_6, rubric4_7]
rubric5 = [rubric5_1, rubric5_2, rubric5_3, rubric5_4, rubric5_5, rubric5_6, rubric5_7]

f1_rubric1 = [[2 for i in range(4)] for j in range(7)]
for i in range(7):
    for j in range(4):
        fp = rubric1[i][j*2]
        fn = rubric1[i][j*2+1]
        tp = rubric1_total - fn
        if fp + fn == eval(f"n1_{i+1}_{j+1}"):
            f1 = calculate_f1_score(tp, fp, fn)
            f1_rubric1[i][j] = f1
        else:
            f1_rubric1[i][j] =  eval(f"n1_{i+1}_{j+1}")-fp-fn

f1_rubric2 = [[2 for i in range(4)] for j in range(7)]
r = 2
for i in range(7):
    for j in range(4):
        fp = rubric2[i][j*2]
        fn = rubric2[i][j*2+1]
        tp = rubric2_total - fn
        if fp + fn == eval(f"n{r}_{i+1}_{j+1}"):
            f1 = calculate_f1_score(tp, fp, fn)
            f1_rubric2[i][j] = f1
        else: 
            f1_rubric2[i][j] = eval(f"n{r}_{i+1}_{j+1}")-fp-fn


       
f1_rubric4 =  [[2 for i in range(4)] for j in range(7)]
r = 4
for i in range(7):
    for j in range(4):
        fp = rubric4[i][j*2]
        fn = rubric4[i][j*2+1]
        tp = rubric4_total - fn
        if fp + fn == eval(f"n{r}_{i+1}_{j+1}"):
            f1 = calculate_f1_score(tp, fp, fn)
            f1_rubric4[i][j] = f1
        else:
            f1_rubric4[i][j] = eval(f"n{r}_{i+1}_{j+1}")-fp-fn
    
f1_rubric5 = [[2 for i in range(4)] for j in range(7)]
r = 5
for i in range(7):
    for j in range(4):
        fp = rubric5[i][j*2]
        fn = rubric5[i][j*2+1]
        tp = rubric5_total - fn
        if fp + fn == eval(f"n{r}_{i+1}_{j+1}"):
            f1 = calculate_f1_score(tp, fp, fn)
            f1_rubric5[i][j] = f1
        else:
            f1_rubric5[i][j] = eval(f"n{r}_{i+1}_{j+1}")-fp-fn

f1_rubric1 = [[round(x, 3) for x in row] for row in f1_rubric1]
f1_rubric2 = [[round(x, 3) for x in row] for row in f1_rubric2]
f1_rubric4 = [[round(x, 3) for x in row] for row in f1_rubric4]
f1_rubric5 = [[round(x, 3) for x in row] for row in f1_rubric5]

row_names = [
    "llama3.2:1b-instruct-fp16",
    "llama3.2:3b-instruct-fp16",
    "llama3.1:8b-instruct-fp16",
    "llama3.1:70b-instruct-q4\_0",
    "llama3.1:70b-instruct-fp16",
    "llama3.1:405b-instruct-q4\_0",
    "gpt4o",
]
col_names = [
    "detailed prompt with examples",
    "simple prompt with examples",
    "detailed prompt with no examples",
    "simple prompt with no examples",
]

print(generate_latex_table(f1_rubric5, row_names, col_names, "Identify and address misconception"))
