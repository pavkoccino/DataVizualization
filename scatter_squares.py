import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [pow(x, 3) for x in x_values]

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-talk')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=14, c=y_values, cmap=plt.cm.Blues)
# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
