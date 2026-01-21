# sort() can sort both umbers and alphabets
# sorting 1-D
import numpy as np
d=np.array([34,21,8,1,0,32])
sorted_d=np.sort(d)
# print(sorted_d)

d_alpha=np.array(["a","k","b","c","z","c"])
sorted_d_alpha=np.sort(d_alpha)
print(sorted_d_alpha)

d_alpha=np.array(["a","Z","k","b","B","c","z","c"])
sorted_d_alpha=np.sort(d_alpha)
print(sorted_d_alpha) #phly saary capital letters valy phir saary small letters valy

d_alpha=np.array(["banana","apple","cherry"])
sorted_d_alpha=np.sort(d_alpha) #alphabatically
print(sorted_d_alpha)

d_alpha=np.array([True,False,False,True])   
sorted_d_alpha=np.sort(d_alpha)
print(sorted_d_alpha)   #false means 0 and true means 1, 0 phly ata h and 1 baad m

# !!!!!!!!!!!!!!!!!!!!!!!!!1   sorting 2-D   !!!!!!!!!!!!!!!!!!!!!!!
dd=np.array([[132,1,4],
             [67,0,99]])
dd_sort=np.sort([dd])
print(dd_sort)


dd=np.array([[132,1,4],
             [67,0,99]])
dd=np.sort([dd])
print(dd)  #updating original array