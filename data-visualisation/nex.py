import matplotlib.pyplot as plt
import numpy as np

'''Mean of Rubric 1: 0.18157142857142852
Mean of Rubric 1 without examples: 0.23642857142857146
Mean of Rubric 2: 0.3055714285714286
Mean of Rubric 2 without examples: 0.6632857142857143
Mean of Rubric 4: 0.2370714285714286
Mean of Rubric 4 without examples: 0.2887857142857143
Mean of Rubric 5: 0.36807142857142855
Mean of Rubric 5 without examples: 0.4626428571428572'''
# Sample data for 16 bars (8 pairs)
values = [0,4,9,13, 1, 9,0,10]
values_er = [0.18157142857142852, 0.23642857142857146, 0.3055714285714286, 0.6632857142857143, 0.2370714285714286, 0.2887857142857143, 0.36807142857142855,  0.4626428571428572]
# Define the number of pairs and bars per pair
num_pairs = 4
bars_per_pair = 2

# Define colors for the bars (one green and one red per pair)
colors = ['#1f77b4', '#ff7f0e']

# Define the width of the bars
bar_width = 0.35

# Create an index for each pair
indices = np.arange(num_pairs)

# Create the bar chart
plt.figure(figsize=(10, 6))

# Plot each pair of bars
for i in range(num_pairs):
    plt.bar(indices[i] - bar_width/2, values_er[i*2], color=colors[0], width=bar_width, label='Examples provided' if i == 0 else "")
    plt.bar(indices[i] + bar_width/2, values_er[i*2 + 1], color=colors[1], width=bar_width, label='No Examples provided' if i == 0 else "")

# Set x-ticks to be in the center of each pair

tick_labels = [
    'Rubric_1',
    'Rubric_2', 
    'Rubric_4', 
    'Rubric_5'
]
plt.xticks(indices, tick_labels, rotation=45, ha='right', fontsize=10)
# Add labels and title
plt.xlabel('Rubric')
plt.ylabel('Mean of Error Rate')
plt.title('Mean Error Rate of Models with and without Examples')
# Add legend
plt.legend()

# Show the plot
plt.show()
