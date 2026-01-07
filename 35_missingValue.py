# np.isnan(array)
# to find the missing values in array

import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])

print(np.isnan(arr))

# Note: We can not compare the nan numbers
print(np.nan == np.nan)
