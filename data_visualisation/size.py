import matplotlib.pyplot as plt
import numpy as np

# Manually defined data points for x and y
x =  [1,2,3,4,5,6,7, 1,2,3,4,5,6,7, 1,2,3,4,5,6,7, 1,2,3,4,5,6,7]
y_detailed_ex = [0, 0.238, 0.429, 0.711, 0.732, 0.750, 0.739, float('nan'), 0.646, float('nan'), float('nan'), float('nan'), float('nan'), 0.962, 0.524, 0.596, 0.647, 0.776, float('nan'), 0.796, 0.743, 0.073, 0.637, 0.818, 0.717, 0.740, 0.749, 0.840]
y_simple_ex = [0, 0.202, 0.263, 0.552, 0.604, 0.739, 0.750, 0.228, 0.519, float('nan'), float('nan'), float('nan'), float('nan'), 0.901, 0.557, 0.506, 0.557, 0.706, 0.635, 0.812, 0.746, 0.072, 0.660, 0.787, 0.667, 0.718, 0.674, 0.798]# Define colors for each segment of 7 points
colors = ['red', 'green', 'blue', 'orange']

# Create the plot
plt.figure(figsize=(10, 6))

j = 1
# Plot each segment of 7 points with a different color
for i in range(4):
    if j == 3:
        j = j+1
     # Remove NaNs while keeping the structure of the data
    x_segment = x[i*7:(i+1)*7]
    y_segment = y_detailed_ex[i*7:(i+1)*7]
    valid_indices = ~np.isnan(y_segment)
    x_clean = np.array(x_segment)[valid_indices]
    y_clean = np.array(y_segment)[valid_indices]

    # Plot the cleaned data
    plt.plot(
        x_clean,  # x values for the cleaned segment
        y_clean,  # y values for the cleaned segment
        color=colors[i],  # color for the segment
        marker='o',  # marker style
        label=f'Rubric {j}'
    )
    j += 1

# Add labels and title
plt.xlabel('Models sorted from smallest to largest')
plt.ylabel('F1 Score')
plt.title('F1 score correlated with Model Size for each Rubric')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
