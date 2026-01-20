import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_array=x.reshape(4,3)   #yani 4rows and 3 columns vala new_array bna do x s, but x chnage
# nhi ho ga of course
# print(new_array)


# convert 1-D to 3-D
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=x.reshape(2,2,3) #yani two 2-D arrays bnao or hr 2-D k ander two 1-D array ho or hr 1-D
# k ander 3 elements hu
z=x.reshape(3,2,2) # yani three 2-D arrays bnao , hr 3-D k ander two 1-D yani two rows hu or
# hr 1-D k ander 2 element hu yani 2 col hu (total ko 3 parts m divide kro, phir jo 
# 3 parts ay un m s hr part ko 2 2 parts m mazeed divide kro or jo parts 
# bny un m 2 2 elements dikhao )
print(y)
# print(z)

#  ERROR
# x=np.array([1,2,3,4,5,6,7,8,9])
# dd=x.reshape(2,4)
# print(dd)   #it will raise error

#   !!!!!!!!!!!  COPY AND VIEW IN RESHAPED ARRAY  !!!!!!!!!!!!!!!!!!!!!
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
dd=a.reshape(2,6)
print("original reshaped array = \n",dd)
copied_reshaped=dd.copy() #copied_reshaped m change krny s dd m changes nhi ho ga
copied_reshaped[0,0]=3642
print("copied array = ")
print(copied_reshaped) 
print("original reshaped array after changes in copied array = \n", dd)

#   !!! view  !!!
print("change in reshaped array will reflect changes in viewed array")
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
dd=a.reshape(2,6)
print("original reshaped array = \n",dd)
view_reshaped=dd.view() #copied_reshaped m change krny s dd m bhi changes ho ga
view_reshaped[0,0]=3642
print("viewed reshaped array = ")
print(view_reshaped) 
print("original reshaped array after changes in viewd reshaped array = \n",dd)

#   !!!!!!!!!!!!!!!!  unknown dimention  !!!!!!!!!!!!!!!!!!!!!!!!!!
# jab ap ki array bhhtt lmbi ho or ap ko na pta ho last valy diemntion ka, yani y na 
# pta ho k kitny kitny elements ay gy ek 1-D k ander to hm -1 likh dety , yani vo khud hi 
# kr le ga equally divide

print("unknown diwemntion")
m=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
ddd=m.reshape(2,2,-1)  #yani total ko 2 pr divide kro, phir jo 2 parts ay un parts ko
# phir 2 2 pr divide kro 
print(ddd)


#   !!!!!!!!!!!!!!  flattening rehsping yani 3-D to 1-D or 2-D to 1-D ...  !!!!!!!!!!
dd=np.array([[1,2,3],
             [4,5,6]]) #chahy yhan 100-D array hi q na ho, bas d=dd.reshape(-1) s 1-D m 
# convert ho jay ggi
d=dd.reshape(-1)
print(d) 