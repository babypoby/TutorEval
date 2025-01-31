import matplotlib.pyplot as plt
import numpy as np

# Define the points (x, y)
x = np.array([0.447, 0.814, 0.710])  # x-coordinates
y = np.array([0.263, 0.767, 0.829])  # y-coordinates


points = [
    (0.447, 0.263, 'Bridge Novice', '#1f77b4'),
    (0.814, 0.767, 'Bridge Expert', '#ff7f0e'),
    (0.710, 0.829, 'MathDial', '#2ca02c')
]

# Extract x, y coordinates, labels, and colors
x = np.array([p[0] for p in points])
y = np.array([p[1] for p in points])
labels = [p[2] for p in points]
colors = [p[3] for p in points]

# Perform linear regression to find the best-fit line
coefficients = np.polyfit(x, y, 1)  # Degree 1 for a linear fit
best_fit_line = np.poly1d(coefficients)

# Generate y values for the best-fit line
x_line = np.linspace(min(x), max(x), 100)  # Generate 100 points between min and max of x
y_line = best_fit_line(x_line)
slope, intercept = coefficients
line_equation = f"y = {slope:.2f}x + {intercept:.2f}"
# Create the plot
plt.figure(figsize=(8, 6))

# Plot each point with its respective color and label
for xi, yi, label, color in points:
    plt.scatter(xi, yi, color=color, label=label, s=150)

# Plot the best-fit line
plt.plot(x_line, y_line, color='gray', label='Best-fit line')
plt.text(0.6, 0.7, line_equation, color='black', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))
# Add labels, title, and grid
plt.xlabel('Model Score')
plt.ylabel('Human Score')
plt.title('Correlation between Model and Human Scores for Rubric 5')
plt.grid(True)
plt.legend()

# Display the plot
plt.show()