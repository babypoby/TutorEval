
import matplotlib.pyplot as plt
import numpy as np

# x are model scores, y are human scores, and labels are the names datasets
points = [
    (0.293, 0.390, 'Bridge Novice', '#1f77b4'),
    (0.5, 0.574, 'Bridge Expert', '#ff7f0e'),
    (0.087, 0.175, 'MathDial',  '#2ca02c')
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

# Equation of the best-fit line
slope, intercept = coefficients
line_equation = f"y = {slope:.2f}x + {intercept:.2f}"

# Create the plot
plt.figure(figsize=(8, 6))

# Plot each point with its respective color and label
for xi, yi, label, color in points:
    plt.scatter(xi, yi, color=color, label=label, s=150)

# Plot the best-fit line
plt.plot(x_line, y_line, color='gray', label='Best-fit line')
plt.text(0.25, 0.3, line_equation, color='black', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

# Add labels, title, and grid
plt.xlabel('Model Score')
plt.ylabel('Human Score')
plt.title('Correlation between Model and Human Scores for Rubric 4')
plt.grid(True)
plt.legend()

# Display the plot
plt.show()