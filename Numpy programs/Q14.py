#Array of duplicate values. Find and display only unique values of the array 
import numpy as np
arr = np.array([1,2,3,4,1,2,3,5,6,7,8,9,10])
unique_values = np.unique(arr)
print("unique values:",unique_values)