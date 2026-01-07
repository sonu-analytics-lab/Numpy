'''
np.delete (array,index, axis=none)
fltten array

'''
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
new_arr = np.delete(arr, 2)
print(new_arr)

# 2d array deleting

arr_2d = np.array([[1, 2], [3, 4], [5, 6]])

new_arr2 = np.delete(arr_2d, 0, axis=0)

print(new_arr2)
