# truncate(trunc()), fix() ---> y dono point k baad vali ko khatam kr de gi lekin return 
# ek float hi kry gi
import numpy as np
rounded=np.trunc([3.176, -3.667]) #
print(rounded)  
print(rounded.dtype)  #float

# fix()
rounded=np.fix([3.176, -3.667]) #
print(rounded)  
# print(rounded.dtype)  #float

# rounding()
# yhan ap y bhi btaty ho k kitny decimal place tak round off krna h(default is 0)
# decimal point is (.)

# 1 decimal place means that there will be 1 digit after decimal point
value=3.126743
# rounded=print("rounded to 0 decimal place",np.around(value))
print("rounded to 1 decimal place = ",np.around(value,1))

# np.around and np.round are the exact same function; np.around is an 
# alias for np.round. They perform identical operations and can be used interchangeably in NumPy. 

# if we have to round off to 1 decimal point and there will be 6 (or value equal to or 
# greater than 5) on 2nd digit after decimal, then value will be incremented by 1:
# like below
value=3.1678 
print("rounded to 1 decimal place = ", np.round(value, 1))
print("rounded to 2 decimal place = ", np.round(value, 2))
print("rounded to 0 decimal place = ", np.round(value))

val=3.89932 
print("rounded off to 0 decimal place = ", np.round(val))
print("rounded off to 1 decimal place = ", np.round(val, 1))

valu=3.9987808
print("rounding to 0 decimal point= ", np.around(valu))
print("rounding to 1 decimal point= ", np.around(valu,1))


# !!!!!!!!!!!!!!!!!!!!   CEIL , FLOOR    !!!!!!!!!!!!!!!!!
# BOTH SHIFT VALUE TO THE NEAREST WHOLE NUMBER

# floor()  (it rounded off decimal to the nearest lower integer)
d=np.floor([-3.8788, 3.4839876])
print(d)  #ab -3 ka lower -4 h or 3.4839876 ka lower 3 h 

dd=np.floor([-3.221, 3.221])  #-3.221 ka lower -4 h or 3.221 ka lower 3 h
print(dd)

# Ceil (The ceil() function rounds off decimal to nearest upper integer.)
d=np.ceil([-3.8788, 3.4839876])
print(d)  #ab -3 ka upper -3 h or 3.4839876 ka upper 4 h 

dd=np.ceil([-3.221, 3.221])  #-3.221 ka upper -3 h or 3.221 ka upper 4 h
print(dd)

dd=np.ceil([-3.221, 3.0]) 
print(dd)


