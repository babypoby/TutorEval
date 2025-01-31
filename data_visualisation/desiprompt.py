import matplotlib.pyplot as plt
import numpy as np

# Sample data for 16 bars (8 pairs)
values = [0.115, 0.248, 0.241, 0.37,  0.23, 0.244, 0.355, 0.381]  # Random values for demonstration; replace with your data

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
    plt.bar(indices[i] - bar_width/2, values[i*2], color=colors[0], width=bar_width, label='Detailed Prompt' if i == 0 else "")
    plt.bar(indices[i] + bar_width/2, values[i*2 + 1], color=colors[1], width=bar_width, label='Simple Prompt' if i == 0 else "")

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
plt.title('Mean Error Rate of Models with Detailed VS Simple Prompt' )

# Add legend
plt.legend()

# Show the plot
plt.show()
