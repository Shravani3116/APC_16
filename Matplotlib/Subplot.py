
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 25]

# First subplot
plt.subplot(2, 1, 1)
plt.plot(x, y1, color='blue', marker='o')
plt.title("Line Plot")
plt.ylabel("Values")

# Second subplot
plt.subplot(2, 1, 2)
plt.bar(x, y2, color='orange')
plt.title("Bar Plot")
plt.xlabel("X-axis")
plt.ylabel("Values")

plt.tight_layout()
plt.show()
