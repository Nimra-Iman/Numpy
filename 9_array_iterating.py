import numpy as np
d=np.array([1,2,3,4,5])
for i in d:
    print(i)

print("iterating 2-D")
dd=np.array([[1,2,3,4,5],
            [6,7,8,9,0]])
for i in dd:
    print(i)  #0th 1-D array (for 1st iteration)
    for j in i:
        print(j)  #each element of 0th 1-D array (for 1st itaeration)

print('itearting 3-D')
ddd=np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[10,11,12]]])
for i in ddd:
    print(i) #[[1,2,3],[4,5,6]]
    for j in i:
        print(j) #[1,2,3]
        for k in j:
            print(k) #1,2,3

print("iterating 3-D another example")
d_d_d=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
for i in d_d_d:
    print("i=\n",i) #[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    for j in i:
        print("j=\n",j) #[1,2,3]
        for k in j:
            print("k=\n",k) # 1,2,3

#  !!!!!!!!!!!!!!  nditer()  !!!!!!!!!!!!!!!!!!!!!!
print("via nditr()")
d_d_d=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
for i in np.nditer(d_d_d):
    print(i) 

print("we can also pass conditions in nditr() like below:") 
d_d_d=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
for i in np.nditer(d_d_d[:,::1]):
    print(i) 



