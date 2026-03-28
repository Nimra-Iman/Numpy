import numpy as np
# splitting involves breaking of array
x=np.array([1,2,3,4,5,6,7,8])
splitted=np.array_split(x,2) #yani "x" array ko split kr do 2 parts k ander
print(splitted)   
print(splitted[0])   

split_unequal=np.array_split(x,3)
split_unequal2=np.array_split(x,5)
print(split_unequal)
print(split_unequal2)

print(split_unequal[0])  # is trah ek ek alag alag array ko utha len gy ta k use kr skyn


#   !!!!!!!!!!!!  splitting  2-D array  !!!!!!!!!!!!!!!!!!!!
print("splitting  2-D array ")
dd=np.array([[1,2],
             [3,4],
             [5,6],
             [7,8]])
# print(dd)

# splitting above one 2-D array into two 2-D arrays
splited_dd=np.array_split(dd,2)
print(splited_dd)
f_2d=(splited_dd[0])

bifurcated_f2d=np.array_split(f_2d,2)
print(bifurcated_f2d)


# ALSO APPLY JOINING CONCEPTS IN IT INCLUDING   HSTACK, AXIS ETC ETC




