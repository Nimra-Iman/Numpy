import numpy as np
# trignometric functions like sin, cos, tan etc take radina as an input
# print(np.sin(0))
# print(np.sin(np.pi))
# print(np.cos(np.pi))
# print(np.tan(0))

#  ---------------  Convert Degrees Into Radians
arr=np.array([1,2,3,4,5])
a=np.deg2rad(arr)
print(a)

print(np.deg2rad(180))

# --------------  Convert radin Into degree
arr=np.array([np.pi,np.pi/2])
print(np.rad2deg(arr))

# --------------------  finding angles:
# Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, 
# arccos, arctan).

# NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for
# corresponding sin, cos and tan values given.

print(np.arcsin(1.0))
print(np.arccos(1.0))
print(np.arctan(1.0))


# ------------------  finding hypotenous
base=3
perpendicular=4
hypotenous= np.hypot(base,perpendicular)
print(hypotenous)
