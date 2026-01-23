#   ----------------------  sum
import numpy as np
a=np.array([1,2,3,4])
b=np.array([1,2,3,4])
c=np.add(a,b)
# print(c)


#  -------------------  subtract
a=np.array([1,2,3,4])
b=np.array([11,12,13,14])
c=np.subtract(a,b) #(means a-b)
# print(c)

#  --------------- multiply
a=np.array([1,2,3,4])
b=np.array([11,12,13,14])
c=np.multiply(a,b) #(means a*b)
print(c)

# ------------ divide
a=np.array([1,2,3,4])
b=np.array([11,12,13,14])
c=np.divide(a,b) #(means a/b)
# print(c)


# ----------------  remainder
a=np.array([1,2,3,4])
b=np.array([11,12,13,14])
c=np.remainder(a,b) #(means a/b and tell reminder, yani "a" ander jay ga)
# print(c)

#  --------------------  modulas
a=np.array([12,2,3,4])
b=np.array([2,12,13,14])
c=np.mod(a,b) #(same as that of remainder)
# print(c)

#--------------- power
a=np.array([1,2,3,4])
b=np.array([1,2,3,4])
c=np.power(a,b) #(means a**b)
# print(c)

#  ------------  absolute
a=np.array([1,2,3,4,67,-3,-6,-98])
c=np.absolute(a) 
# print(c)

# ---------------  divmod
# divmod gives both divide and mod/remainder vales
a=np.array([22,24,28,20])
b=np.array([2,4,6,8])
c=np.divmod(a,b)   #output m phli array divide ka answer de gi yani quotient
# de gi or 2nd array remainder de gi
print(c)