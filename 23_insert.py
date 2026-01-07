'''
np.insert(array, index , value, axis=none)
array   = orginal array
index   = position no where we want to insert the number
value   = actual data
axis    = none-flatten or in 2d 0=row, =columns

'''
import numpy as np

# arr = np.array([10, 20, 30, 40, 50, 60])
# new_arr = np.insert(arr, 2, 100)
# print(new_arr)

# insert in 2d

arr_2d = np.array([[1, 2], [3, 4]])
new_arr_2d = np.insert(arr_2d, 1, [5, 6], axis=0)
print(new_arr_2d)
'''
axis=0 : ouuput 
[[1 2]
 [5 6]
 [3 4]]
axis=1 : ouuput 
[[1 5 2]
 [3 6 4]]

axis=none : ouuput  
[1 5 6 2 3 4]
'''
