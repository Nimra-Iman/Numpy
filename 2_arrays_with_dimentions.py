import numpy as np
# ndarray: any array object in numpy called ndarray

x=np.array([1,2,3]) #yani hm n array class ka ek object hi to bnaya and this
# object is called ndarray
print(x)
print(type(x)) #<class 'numpy.ndarray'>

# we can pass lists,tuples or any other array and it will converted to ndarray
y=np.array((1,2,3)) #tuple
print(y)

#   !!!!!!!!!!!  DIMENTIONS OF ARRAY  !!!!!!!!!!!!!!!!!!!!
# DIMENTIONS IN ARRAY IS ONE LEVEL OF ARRAY DEPTH (nested arrays)
# 0-D array: 
z=np.array(42) #In Python, a scalar is a single value or data item, as opposed to an 
# array or matrix which can hold multiple values.
print(z)

# 1-D array: an array that has 0-D as its elements called 1-D or unidimentional array
z=np.array([1,2,3]) #this is most common
print(z)

#2-D array: (contains multiple 1-D arrays)
x=np.array([[1,2,3],[3,4,5]])
print(x)

# 3-D array: we will pass two 2-D arrays here
ddd=np.array([[[22,33,44],[44,55,66]],
              [[77,88,99],[99,88,77]]])
print(ddd)

#  !!!!!!!!!!!!  checking how many dimentions the array have (use ndim attribute)
print(ddd.ndim) # 3 (yani 3 dimentional array, isi trah ap 1-D,2-D,3-D check kr skty ho)

# !!!!!!!  create an array of 5 dimentions :
ddddd=np.array([1,2,3,4,5],ndmin=5)
print(ddddd)
print(ddddd.ndim)



