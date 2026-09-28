import numpy as np

# Create a random 3D array
A = np.random.randint(1, 101, size=(2, 3, 4))

print("Original array:")
print(A)

# Replace values greater than 50 with 0
A[A > 50] = 0

print("\nAfter replacing values greater than 50 with 0:")
print(A)