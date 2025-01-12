import matplotlib.pyplot as plt
import numpy as np

# Data
categories = [
    "Don't reveal answer",
    "Promote active engagement",
    "Communicate with positive tone",
    "Identify and address misconception",
]


points_1 = [
    (0.766, 0.681, 'Bridge 1', 'red'),
    (0.941, 0.902, 'Bridge 2', 'green'),
    (0.963, 0.982, 'MathDial', 'blue')
]

points_2 = [
    (0.236, 0.255, 'Bridge 1', 'red'),
    (0.697, 0.697, 'Bridge 2', 'green'),
    (0.864, 0.927, 'MathDial', 'blue')
]

points_4 = [
    (0.293, 0.390, 'Bridge 1', 'red'),
    (0.5, 0.574, 'Bridge 2', 'green'),
    (0.087, 0.175, 'MathDial', 'blue')
]

points_5 = [
    (0.447, 0.263, 'Bridge 1', 'red'),
    (0.814, 0.767, 'Bridge 2', 'green'),
    (0.710, 0.829, 'MathDial', 'blue')
]

bridge1_scores = [0.766, 0.236, 0.293, 0.447]
bridge2_scores = [0.941, 0.697, 0.5, 0.814]
mathdial_scores = [0.963, 0.864, 0.087, 0.710]
learnlm_scores = [0.67, 0.95, 0.77, 0.75]
gemini_scores = [0.82, 0.79, 0.74, 0.5]

# Bar width and positions
bar_width = 0.15
y_positions = np.arange(len(categories))

# Create horizontal bar chart
plt.figure(figsize=(12, 6))
plt.barh(y_positions - 2* bar_width , bridge1_scores, bar_width, label="Bridge 1")
plt.barh(y_positions - bar_width, bridge2_scores, bar_width, label="Bridge 2")
plt.barh(y_positions, mathdial_scores, bar_width, label="MathDial")
plt.barh(y_positions + bar_width, learnlm_scores, bar_width, label="LearnLM")
plt.barh(y_positions + 2* bar_width, gemini_scores, bar_width, label="Gemini")

# Add x-value labels to each bar
for i in range(len(categories)):
    for j, (score, offset) in enumerate(zip(
            [bridge1_scores, bridge2_scores, mathdial_scores, learnlm_scores, gemini_scores
             ],
            [-2, -1, 0, 1, 2]
    )):
        plt.text(score[i], i + offset * bar_width, f"{score[i]:.2f}", ha='left', va='center')  
# Customize chart
plt.yticks(y_positions, categories, fontsize=11)
plt.xlabel("Critic Score (higher is better)", fontsize=11)  # Adjust font size for xlabel
plt.title("Comparison of Tutor Models", fontsize=13)  # Adjust font size for title
plt.legend(fontsize=11)
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()
