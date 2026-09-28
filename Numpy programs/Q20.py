import numpy as np

# Create a (2, 3, 4) array
A = np.arange(1, 25).reshape(2, 3, 4)

print("Array:")
print(A)

# Sum of all elements
print("\nSum of all elements:")
print(np.sum(A))

# Sum of each layer
print("\nSum of each layer:")
print(np.sum(A, axis=(1, 2)))

# Sum along rows
print("\nSum along rows:")
print(np.sum(A, axis=2))

# Sum along columns
print("\nSum along columns:")
print(np.sum(A, axis=1))