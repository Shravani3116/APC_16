#Create two NumPy arrays and concatenate them horizontally and vertically.
import numpy as np
A = np.array([[1,2],[3,4]]) 
B = np.array([[5,6],[7,8]])
C = np.concatenate((A, B), axis=0)
D = np.concatenate((A, B), axis=1)
print("Horizontal Concatenation:")
print(D)
print("\nVertical Concatenation:")
print(C)
