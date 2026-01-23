# ufuncs stands for universal 
# in numpy array, there are some functions that are ufuncs. all numpoy fuinctions are not
# ufuncs
# --> ufuncs perform vectorisation
# --> ufuncs are very fast as compared to python lists because internally C-Language was working 
# --> vectorisation means to perform working on all array elements in once, instead of perfroming
#  operation in a[0] and a[1] at a time and the wait to complete its execution to start working on
#  a[1] and b[1] for example. Vectorization avoids explicit Python loops and applies operations to 
# entire arrays at once.





# agar hm n normal 2 lists k elements ko add kr k kisi doosri list m daalny hn to hmy
# ek ek element ko iterate krna ho ga, lekin agar hm vectorization ko use krty hn to
# hm is kaam ko bhhtt fastly kr skty hn

# vactorization: Converting iterative statements into a vector based operation is
# called vectorization.

# using normal way:
a=[1,2,3,4]
b=[1,2,3,4]
z=[]
for i,j in zip(a,b):
    z.append(i+j)
# print(z)

# we will use ufuncs to make this work more fast:
# ufuncs are used to implement vectorization in NumPy which is way faster than 
# iterating over elements
import numpy as np
a=[1,2,3,4]
b=[1,2,3,4]
z=np.add(a,b) #1st it will convert lists to array and then perform operation 
print(z.shape)


# NumPy functions auto-convert lists to arrays, but Python operators do not.

a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5])
c = np.add(a,b)
print(c.shape)

# ufuncs also take additional arguments, like:
# where boolean array or condition defining where the operations should take place.
# dtype defining the return type of elements.
# out output array where the return value should be copied.