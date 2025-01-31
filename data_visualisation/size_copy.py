import matplotlib.pyplot as plt
import numpy as np

# Manually defined data points for x and y
x =  [1,2,3,4,5,6,7, 1,2,3,4,5,6,7, 1,2,3,4,5,6,7, 1,2,3,4,5,6,7]
y = [0.121, 0.309, 0.155, 0.063, 0.053, 0.048, 0.058, 0.684, 0.403, 0.273, 0.091, 0.104, 0.078, 0.052, 0.54, 0.364, 0.182, 0.131, 0.131, 0.116, 0.146, 0.65, 0.414, 0.255, 0.331, 0.318, 0.299, 0.217]
oneminusy = [1 - i for i in y]
y_simple = [0.126, 0.725, 0.541, 0.126, 0.101, 0.058, 0.058, 0.675, 0.489, 0.818, 0.186, 0.169, 0.126, 0.130, 0.34, 0.424, 0.273, 0.177, 0.192, 0.131, 0.172, 0.656, 0.408, 0.287, 0.369, 0.325, 0.363, 0.261]
oneminusy_simple = [1 - i for i in y_simple]
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
    y_segment = oneminusy_simple[i*7:(i+1)*7]
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
plt.ylabel('Accuracy')
plt.title('Accuracy correlated with Model Size for each Rubric')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
