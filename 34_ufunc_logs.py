# numpy just provide facility to get log of an element at base 10,e,2

#!!!!!!!!!!!!!!!!1   All of the log functions will place -inf or inf in the elements
#  if the log can not be computed.  !!!!!!!!!!!!!!!!!!!!!1
import numpy as np

# ---------------  calculating log at base 10
d=np.array([23,34,45,1,10])
print(np.log10(d)) #yani d k hr ek ek element ka log10 print kro

print()
print()
# ---------------  calculating log at base 2
print("calculating log at base 2")
d=np.array([34,2,1,0,97,43]) #ab 0 pr -inf show ho rha, yani is ka log nhi le skty,log of
# 0 at any base is undefined
print(np.log2(d))


# ------------------- calculating natural log (log at base e)
dd=np.array([1,2,3,4,5,6])
print(np.log(dd))


# -----------  we can get log of element at any abse by creating our own ufuncs
print("we can get log of element at any abse by creating our own ufuncs")
from math import log
def calculate_log(given_array):
    print(log(given_array,90))  #calculte log of given array with base 90

dd=np.frompyfunc(calculate_log, 1,1)
dd([34,1,2,4,5]) #calculate log of each element with base 90


# !!!!!!!!!!!!!!!!!!!!!! another example
print("calculate log of 100 with base 90")
from math import log
import numpy as np
ddd=np.frompyfunc(log, 2,1)
print(ddd(100,90)) #calculate log of 100 with base 90

# !!!!!!!!!!!!!!!!  another example
import math
def logg(array,base):
    print(math.log(array,base))
d=np.frompyfunc(logg,2,1)

d(np.array([2,4,5,3,2,1]),9)


