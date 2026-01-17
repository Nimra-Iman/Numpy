# INDEXING and SLICING ki bat kryn to indexing drops dimention and slicing keeps
# the dimention same as of original array. Colon : ka use krny s hm slicing krty hn
# agr rows and column dono m : use kia, yani dono m slicing ki to dimention same rhy gi
# # Agar kisi axis (row ya column) mein single number use karein (INDEXING)
# to us axis ki dimension drop ho jati hai
# e.g: if we have 2D array and we do this: 
# a[:, 0:1]   #  then keeps 2D (column slice)
# a[:, 0]     # then becomes 1D





import numpy as np
# accessing 1-D
d=np.array([22,33,44])
# print(d[-2])
# print(d[0])
print(d[1] + d[2])


#  accessing 2-D 
dd=np.array([[22,33,44], #first row
             [33,44,55]]) #2nd row
# print(dd[0,1]) #0=row,, 1=column  (yani 0th row ka 1st elemnt because 1st elemrnt column1 m
# # lie kr rha h)
# print(dd[1,1]) #yani 1st row 1st column pr jo elemnt pra vo de do

print(dd[0])  #0th row ful mil jay gi

#  accessing 3-D (combing two 2-Ds)
ddd=np.array([[[22,33,44],[21,31,41]], #[22,33,44] is 0th row and [21,31,41] is 1st row of 0th vala 2-D
              [[44,55,66],[77,88,99]]])

print(ddd[0, 0, 1]) #yani 0th vali 2-D m 0th row pr or 1st col pr jo elemnt pra
print(ddd[1,1,1])



#   ****************   IMPORTANT CONCEPTS  ********************************
d2 = np.array([[1,2,3],
            [5,6,7]])
print(d2[1,1])
print(d2[1,1:-1])  #shape 1D  q k ek m indexing kr rhy hn
print(d2[1:,1:-1]) # shape 2d q k dono m slicing ho rhi h, if you want k shape chnage 
# na ho to try to use slicing with all

d3 = np.array([[[1,2,3],[4,5,6]],
                [[11,22,33],[21,21,21]]])
print(d3[1, 0, 1])

print(d3[ 1, 0, 0:2 ])  #shape becomes 1D 
print(d3[ 1, 0:, 0:2 ])  #shape becomes 2D
print(d3[ 1:, 0:, 0:2 ])  #shape becomes 3D



# zum Biespiele: 
import numpy as np

a = np.array([[10, 20, 30],
              [40, 50, 60]])

print(a[0])   #[10,20,30]

print(a[0:1])  # [[10,20,30]]

print(a[:, 1])  # [20 50]

print(a[:, 1:2])   # [[20],[50]]

print(a[1:, 0:2])    # [[40 50]]
#making long story short, age kisi ek jga bhi indexing kr di, us jga ki bracket km ho jay gi

b = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[10,11,12]]])

print(b[1,0,2])   #9 

print(b[1,0,0:2])  #[7 8]

print(b[1,0:,0:2] )  #[[7 8][10 11]]

print(b[1:,0:,0:2])  # [[[7 8][10 11]]]
print( b[:,1,1])   # [5 11]



