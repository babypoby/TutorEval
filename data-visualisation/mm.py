

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        # Wenn die Anzahl der Zahlen gerade ist, ist der Median der Durchschnitt der beiden mittleren Zahlen
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        # Wenn die Anzahl der Zahlen ungerade ist, ist der Median die mittlere Zahl
        return sorted_numbers[mid]
    
'''\begin{table}
\begin{center}
\begin{tabular}{ |>{\centering\arraybackslash}m{3cm}|>{\centering\arraybackslash}m{2.75cm}|>{\centering\arraybackslash}m{2.75cm}|>{\centering\arraybackslash}m{2.75cm}|>{\centering\arraybackslash}m{2.75cm}| }
\hline
 & detailed prompt with examples & simple prompt with examples & detailed prompt with no examples & simple prompt with no examples \\
\hline
\texttt{llama3.2:1b-\newline instruct-fp16} & $\frac{25}{207} \approx 0.121$ & $\frac{26}{207} \approx 0.126$ & $\frac{40}{207} \approx 0.193$ & $\frac{54}{207} \approx 0.261$ \\ 
\hline
\texttt{llama3.2:3b-\newline instruct-fp16} & $\frac{64}{207} \approx 0.309$ & $\frac{150}{207} \approx 0.725$ & $\frac{70}{207} \approx 0.338$ & $\frac{100}{207} \approx 0.483$ \\
\hline
\texttt{llama3.1:8b-\newline instruct-fp16} & $\frac{32}{207} \approx 0.155$ & $\frac{112}{207} \approx 0.541$ & $\frac{113}{207} \approx 0.547$ & $\frac{181}{207} \approx 0.874$ \\
\hline
\texttt{llama3.1:70b-\newline instruct-q4\_0}
& $ \frac{13}{207} \approx 0.063 $ 
& $ \frac{26}{207} \approx 0.126 $ 
& $ \frac{12}{207} \approx 0.058 $ 
& $ \frac{15}{207} \approx 0.073 $ \\
\hline 
\texttt{llama3.1:70b-\newline instruct-fp16} & $ \frac{11}{207} \approx 0.053 $ & $ \frac{21}{207} \approx 0.101 $ & $ \frac{10}{207} \approx 0.048 $ & $ \frac{18}{207} \approx 0.087 $ \\
\hline 
\texttt{llama3.1:405b-\newline instruct-q\_40} & $\frac{10}{207} \approx 0.048$ & $\frac{12}{207} \approx 0.058$ & $\frac{14}{207} \approx 0.068$ & $\frac{22}{207} \approx 0.106$ \\
\hline
\texttt{gpt4o} & $\frac{12}{207} \approx 0.058$ & $\frac{12}{207} \approx 0.058$ & $\frac{18}{207} \approx 0.087$ & $\frac{18}{207} \approx 0.087$ \\
\hline
\end{tabular}
\end{center}
\caption{Error rate of Models for Rubric “Do not reveal the answer”}
\label{tab:error rate Rubric 1}
\end{table}
\begin{table}
\begin{center}
\begin{tabular}{ |>{\centering\arraybackslash}m{3cm}|>{\centering\arraybackslash}m{2.75cm}|>{\centering\arraybackslash}m{2.75cm}|>{\centering\arraybackslash}m{2.75cm}|>{\centering\arraybackslash}m{2.75cm}| } 
\hline
 & detailed prompt with examples & simple prompt with examples & detailed prompt with no examples & simple prompt with no examples \\
\hline
\texttt{llama3.2:1b-\newline instruct-fp16} & $\frac{158}{231} \approx 0.684$ & $\frac{156}{231} \approx 0.675$ & $\frac{215}{231} \approx 0.931$ & $\frac{207}{231} \approx 0.896$ \\  
\hline
\texttt{llama3.2:3b-\newline instruct-fp16} & $\frac{93}{231} \approx 0.403$ & $\frac{113}{231} \approx 0.489$ & $\frac{197}{231} \approx 0.853$ & $\frac{231}{231} \approx 1$ \\
\hline
\texttt{llama3.1:8b-\newline instruct-fp16} & $\frac{63}{231} \approx 0.273$ & $\frac{189}{231} \approx 0.818$ & $\frac{229}{231} \approx 0.991$ & $\frac{231}{231} \approx 1$ \\
\hline
\texttt{llama3.1:70b-\newline instruct-q4\_0} & $\frac{21}{231} \approx 0.091$ & $\frac{43}{231} \approx 0.186$ & $\frac{39}{231} \approx 0.169$ & $\frac{109}{231} \approx 0.472$ \\
\hline 
\texttt{llama3.1:70b-\newline instruct-fp16} & $\frac{24}{231} \approx 0.104$ & $\frac{39}{231} \approx 0.169$ & $\frac{28}{231} \approx 0.121$ & $\frac{195}{231} \approx 0.844$ \\
\hline 
\texttt{llama3.1:405b-\newline instruct-q4\_0} & $\frac{18}{231} \approx 0.078$ & $\frac{29}{231} \approx 0.126$ & $\frac{154}{231} \approx 0.667$ & $\frac{207}{231} \approx 0.896$ \\
\hline
\texttt{gpt4o} & $\frac{12}{231} \approx 0.052$ & $\frac{30}{231} \approx 0.130$ & $\frac{40}{231} \approx 0.173$ & $\frac{63}{231} \approx 0.273$ \\
\hline
\end{tabular}
\end{center}
\caption{Error rate of Models for Rubric “Promote active engagement”}
\label{tab:error rate Rubric 2}
\end{table}

\begin{table}
\begin{center}
\begin{tabular}{ |>{\centering\arraybackslash}m{3cm}|>{\centering\arraybackslash}m{2.75cm}|>{\centering\arraybackslash}m{2.75cm}|>{\centering\arraybackslash}m{2.75cm}|>{\centering\arraybackslash}m{2.75cm}| }
\hline
 & detailed prompt with examples & simple prompt with examples & detailed prompt with no examples & simple prompt with no examples \\
\hline
\texttt{llama3.2:1b-\newline instruct-fp16} & $\frac{107}{198} \approx 0.54$ & $\frac{78}{198} \approx 0.34$ & $\frac{138}{198} \approx 0.7$ & $\frac{144}{198} \approx 0.727$ \\  
\hline
\texttt{llama3.2:3b-\newline instruct-fp16} & $\frac{72}{198} \approx 0.364$ & $\frac{84}{198} \approx 0.424$ & $\frac{60}{198} \approx 0.303$ & $\frac{63}{198} \approx 0.318$ \\
\hline
\texttt{llama3.1:8b-\newline instruct-fp16} & $\frac{36}{198} \approx 0.182$ & $\frac{54}{198} \approx 0.273$ & $\frac{35}{198} \approx 0.177$ & $\frac{83}{198} \approx 0.419$ \\
\hline
\texttt{llama3.1:70b-\newline instruct-q4\_0} & $\frac{26}{198} \approx 0.131$ & $\frac{35}{198} \approx 0.177$ & $\frac{39}{198} \approx 0.197$ & $\frac{36}{198} \approx 0.182$ \\
\hline 
\texttt{llama3.1:70b-\newline instruct-fp16} & $\frac{26}{198} \approx 0.131$ & $\frac{38}{198} \approx 0.192$ & $\frac{33}{198} \approx 0.167$ & $\frac{29}{198} \approx 0.146$ \\
\hline 
\texttt{llama3.1:405b-\newline instruct-q4\_0} & $\frac{23}{198} \approx 0.116$ & $\frac{26}{198} \approx 0.131$ & $\frac{26}{198} \approx 0.131$ & $\frac{31}{198} \approx 0.157$ \\
\hline
\texttt{gpt4o} & $\frac{29}{198} \approx 0.146$ & $\frac{34}{198} \approx 0.172$ & $\frac{40}{198} \approx 0.202$ & $\frac{43}{198} \approx 0.217$ \\
\hline
\end{tabular}
\end{center}
\caption{Error rate of Models for Rubric “Communicate with positive tone”}
\label{tab:error rate Rubric 4}
\end{table}

\begin{table}
\begin{center}
\begin{tabular}{ |>{\centering\arraybackslash}m{3cm}|>{\centering\arraybackslash}m{2.75cm}|>{\centering\arraybackslash}m{2.75cm}|>{\centering\arraybackslash}m{2.75cm}|>{\centering\arraybackslash}m{2.75cm}| } 
\hline
 & detailed prompt with examples & simple prompt with examples & detailed prompt with no examples & simple prompt with no examples \\
\hline
\texttt{llama3.2:1b-\newline instruct-fp16} & $\frac{102}{157} \approx 0.65$ & $\frac{103}{157} \approx 0.656$ & $\frac{133}{157} \approx 0.847$ & $\frac{131}{157} \approx 0.834$ \\  
\hline
\texttt{llama3.2:3b-\newline instruct-fp16} & $\frac{65}{157} \approx 0.414$ & $\frac{64}{157} \approx 0.408$ & $\frac{77}{157} \approx 0.490$ & $\frac{83}{157} \approx 0.529$ \\
\hline
\texttt{llama3.1:8b-\newline instruct-fp16} & $\frac{40}{157} \approx 0.255$ & $\frac{45}{157} \approx 0.287$ & $\frac{46}{157} \approx 0.293$ & $\frac{51}{157} \approx 0.325$ \\
\hline
\texttt{llama3.1:70b-\newline instruct-q4\_0} & $\frac{52}{157} \approx 0.331$ & $\frac{58}{157} \approx 0.369$ & $\frac{65}{157} \approx 0.414$ & $\frac{75}{157} \approx 0.478$ \\
\hline 
\texttt{llama3.1:70b-\newline instruct-fp16} & $\frac{50}{157} \approx 0.318$ & $\frac{51}{157} \approx 0.325$ & $\frac{46}{157} \approx 0.293$ & $\frac{60}{157} \approx 0.382$ \\
\hline 
\texttt{llama3.1:405b-\newline instruct-q4\_0} & $\frac{47}{157} \approx 0.299$ & $\frac{57}{157} \approx 0.363$ & $\frac{81}{157} \approx 0.516$ & $\frac{92}{157} \approx 0.586$ \\
\hline
\texttt{gpt4o} & $\frac{34}{157} \approx 0.217$ & $\frac{41}{157} \approx 0.261$ & $\frac{36}{157} \approx 0.229$ & $\frac{41}{157} \approx 0.261$ \\
\hline
\end{tabular}
\end{center}
\caption{Error rate of Models for Rubric “Identify and address misconception”}
\label{tab:error rate Rubric 5}
\end{table}'''


r1 = [ 0.121, 0.309, 0.155, 0.063, 0.053, 0.048, 0.058, 0.126, 0.725, 0.541, 0.126, 0.101, 0.058, 0.058]
r1_nex = [0.193, 0.338, 0.547, 0.058, 0.048, 0.068, 0.087, 0.261, 0.483, 0.874, 0.073, 0.087, 0.106, 0.087]

r2 = [0.684, 0.403, 0.273, 0.091, 0.104, 0.078, 0.052, 0.675, 0.489, 0.818, 0.186, 0.169, 0.126, 0.130]
r2_nex = [0.931, 0.853, 0.991, 0.169, 0.121, 0.667, 0.173, 0.896, 1, 1, 0.472, 0.844, 0.896, 0.273]

r4 = [0.54, 0.364, 0.182, 0.131, 0.131, 0.116, 0.146, 0.34, 0.424, 0.273, 0.177, 0.192, 0.131, 0.172]
r4_nex = [0.7, 0.303, 0.177, 0.197, 0.167, 0.131, 0.202, 0.727, 0.318, 0.419, 0.182, 0.146, 0.157, 0.217]

r5 = [0.65, 0.414, 0.255, 0.331, 0.318, 0.299, 0.217, 0.656, 0.408, 0.287, 0.369, 0.325, 0.363, 0.261]
r5_nex = [0.847, 0.49, 0.293, 0.414, 0.293, 0.516, 0.229, 0.834, 0.529, 0.325, 0.478, 0.382, 0.586, 0.261]


print (f"Mean of Rubric 1: {calculate_mean(r1)}")
print (f"Mean of Rubric 1 without examples: {calculate_mean(r1_nex)}")

print (f"Mean of Rubric 2: {calculate_mean(r2)}")
print (f"Mean of Rubric 2 without examples: {calculate_mean(r2_nex)}")

print (f"Mean of Rubric 4: {calculate_mean(r4)}")
print (f"Mean of Rubric 4 without examples: {calculate_mean(r4_nex)}")

print (f"Mean of Rubric 5: {calculate_mean(r5)}")
print (f"Mean of Rubric 5 without examples: {calculate_mean(r5_nex)}")

print(len(r1))