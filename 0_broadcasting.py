# Now, Py has a feature called Broadcasting. Which allows it to work on an array of
#  different shapes. For example, if we have one array of size 2, 3 and another array 
#  of size 5, then it will broadcast a 1D array of size 5. 

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = np.array([1,2,3])
print(a+b)



# Rule 1:

# 👉 Shapes must match OR one dimension = 1

# Rule 2:

# 👉 NumPy compares from right to left

# Example:

# (2, 3)
# (1, 3) ✅ works
# Rule 3:

# 👉 If dimension = 1 → it gets expanded

# ❌ When it fails
# arr = np.array([[1, 2],
#                 [3, 4]])

# b = np.array([1, 2, 3])

# 👉 Shapes:

# (2,2)
# (3,) ❌

# 👉 Not compatible → error