import numpy as np

# Create random 3D array of shape (3, 4, 5)
A = np.random.randint(1, 101, size=(3, 4, 5))

print("3D Array:")
print(A)

print("\nMean:", np.mean(A))
print("Median:", np.median(A))
print("Standard Deviation:", np.std(A))
print("Variance:", np.var(A))
print("Minimum:", np.min(A))
print("Maximum:", np.max(A))