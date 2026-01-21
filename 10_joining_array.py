import numpy as np
d=np.array([1,2,3])
d0=np.array([4,5,6])
d1=np.concatenate((d,d0))
# print(d1)


# !!!!!!!  concatenate 2-D arrays  !!!!!!!!!!!!!!!!!
dd=np.array([[1,2,3],
            [4,5,6]])

dd1=np.array([[11,12,13],
            [41,51,16]])
dd_new=np.concatenate((dd,dd1),axis=None) #axis=None krny s saary elements mil kr 1-D bnay gy
# means these 2-Ds will convert to one 1-D 
# print(dd_new)

# -----------------------  axis=1
dd=np.array([[1,2,3],
            [4,5,6]])

dd1=np.array([[11,12,13],
            [41,51,16]])
dd_new=np.concatenate((dd,dd1),axis=1) #esa krny s (dd and dd1) yani dono ki 0th row mil
# kr dd_new ki 0th row bnayn gy
print(dd_new)


# ------------------  axis=0 (default)

dd=np.array([[1,2,3],
            [4,5,6]])

dd1=np.array([[11,12,13],
            [41,51,16]])
dd_new=np.concatenate((dd,dd1),axis=0)  #axis=0 krny s y saari 2-D arrays mil kr ek 2-D
# array bnay gi
# print(dd_new)

# the first running vertically downwards across rows (axis 0), and the second running 
# horizontally across columns (axis 1).


#   !!!!!!!!!!!  concatenating  3-D arrays  !!!!!!!!!!!!!!!!!!!!!!!!

# ------------------------axis = None  (convert to 1-D)
ddd0=np.array([[[1,2,3],[4,5,6]],
               [[7,8,9],[10,11,12]]])

ddd1=np.array([[[11,22,33],[44,55,66]],
               [[77,88,99],[100,101,102]]])

ddd_new=np.concatenate((ddd0,ddd1),axis=None)
# print(ddd_new)

# ----------------------  axis = 1 
ddd0=np.array([[[1,2,3],[4,5,6]],
               [[7,8,9],[10,11,12]]])

ddd1=np.array([[[11,22,33],[44,55,66]],
               [[77,88,99],[100,101,102]]])

ddd_new=np.concatenate((ddd0,ddd1),axis=1)
# print(ddd_new)

# -------------------  axis=0
ddd0=np.array([[[1,2,3],[4,5,6]],
               [[7,8,9],[10,11,12]]])

ddd1=np.array([[[11,22,33],[44,55,66]],
               [[77,88,99],[100,101,102]]])

ddd_new=np.concatenate((ddd0,ddd1),axis=0)
# print(ddd_new)


# !!!!!!!!!!!!!!  stack()  !!!!!!!!!!!!!!!!!!!!

d=np.array([1,2,3])
d0=np.array([4,5,6])
d1=np.stack((d,d0),axis=1) #concatenate m axis=1 krny s dono arrays ki 0th 0th row mil
# kr new array ki 0th row bnaty hn lekin stack m yhan pr ek ek index uth kr new array ki
# 1st row bnata h
# print(d1)

d=np.array([1,2,3])
d0=np.array([4,5,6])
d1=np.stack((d,d0),axis=0) #convert this two 1-Ds into one 2-D
# print(d1)

# ------------------  hstack, vstack, dstack (y stack ki mazeed types hn or in k saath
                      # axis bhi show krny ki zrurt nhi hoti)

d=np.array([1,2,3])
d0=np.array([4,5,6])
d1=np.hstack((d,d0)) #hstack yani horizontal, (output==== [1 2 3 4 5 6])
# print(d1)


d=np.array([1,2,3])
d0=np.array([4,5,6])
d1=np.vstack((d,d0)) #vstack yani vertical, (output is same as "stack with axis =0")
# print(d1)


d=np.array([1,2,3])
d0=np.array([4,5,6])
d1=np.dstack((d,d0)) #dstack yani depth(height), (output is same as stack with axis =1)
# print(d1)


# axis = 0 → vertical (rows)
# axis = 1 → horizontal (columns)

# concatenate → never adds a dimension
# stack → always adds exactly one dimension

# hstack → columns
# vstack → rows
# dstack → depth (3rd dimension)


# yani axis = 1 means y horizontally grow kry ga 
# dd=np.array([[1,2,3],
#                   [4,5,6]])
# dd1=np.array([[11,12,13],
#             [41,51,16]])
# print(np.concatenate ((dd,dd1), axis = 1))  # ab y horizontally grow kry ga [[1,2,3,11,12,13],
#                                                                             # [4,5,6,41,51,16]]
