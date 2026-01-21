import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
splitted=np.array_split(x,2) #yani "x" array ko split kr do 2 parts k ander
print(splitted)   

split_unequal=np.array_split(x,3)
split_unequal2=np.array_split(x,5)
print(split_unequal)