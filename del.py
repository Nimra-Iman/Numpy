import numpy as np

# ddd0=np.array([[[1,2,3],[4,5,6]],
#                [[7,8,9],[10,11,12]]])

# ddd1=np.array([[[11,22,33],[44,55,66]],
#                [[77,88,99],[100,101,102]]])

# ddd_new=np.concatenate((ddd0,ddd1),axis=1)
# # print(ddd_new)


# # [[[1,2,3],[4,5,6],[11,22,33],[44,55,66]],
# #  [[7,8,9],[10,11,12],[77,88,99],[100,101,102]]]


# d=np.array([1,2,3])
# d0=np.array([4,5,6])
# d1=np.hstack((d,d0)) #hstack yani horizontal, (output==== [1 2 3 4 5 6])
# # print(d1)


# d=np.array([1,2,3])
# d0=np.array([4,5,6])
# d1=np.vstack((d,d0)) #vstack yani vertical, (output is same as "stack with axis =0")
# print(d1)


# d=np.array([1,2,3])
# d0=np.array([4,5,6])
# d1=np.dstack((d,d0)) #dstack yani depth(height), (output is same as stack with axis =1)
# print(d1)


value=3.1678 
print("rounded to 1 decimal place = ", np.round(value, 1))    #3.2
print("rounded to 2 decimal place = ", np.round(value, 2))     #3.18
print("rounded to 0 decimal place = ", np.round(value))      #3.

val=3.89932 
print("rounded off to 0 decimal place = ", np.round(val))    #4.
print("rounded off to 1 decimal place = ", np.round(val, 1))  #3.9

valu=3.9987808
print("rounding to 0 decimal point= ", np.around(valu))    # 4.
print("rounding to 1 decimal point= ", np.around(valu,1))    #4.


# !!!!!!!!!!!!!!!!!!!!   CEIL , FLOOR    !!!!!!!!!!!!!!!!!
# BOTH SHIFT VALUE TO THE NEAREST WHOLE NUMBER

# floor()  (it rounded off decimal to the nearest lower integer)
d=np.floor([-3.8788, 3.4839876])
print(d)     #-4   3

dd=np.floor([-3.221, 3.221])  
print(dd)    #--4     3  

# Ceil (The ceil() function rounds off decimal to nearest upper integer.)
d=np.ceil([-3.8788, 3.4839876])
print(d)   # 3     4

print(np.ceil([-3.221, 3.221])  )   #-3   4

dd=np.ceil([-3.221, 3.0])  # -3  3
print(dd)


