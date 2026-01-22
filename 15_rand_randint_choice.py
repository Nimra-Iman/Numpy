# random--- something that cannot be predicted logically
# import numpy as np
# random_number=np.random.randint(100)

# randint, rand, choice

import numpy as np
from numpy import random
random_number=random.randint(100)  #yani 100 tak koi bhi random number generate kro
print(random_number)  


random_number=random.rand()  # 1 float value generate ho gi
print(random_number) 

random_numbers=random.rand(5)  # 5 float values generate ho gi
print(random_numbers) 


# generating an integer random 1-D array that contains random 5 elements from 0 to 99
random_1_D=random.randint(100, size=(5))
print(random_1_D)

# generating an integer random 2-D array that contains 2 rows with random 2 elements from 0 to 99
random_2_D=random.randint(100, size=(2,2))
print(random_2_D)


# generating an integer random 3-D array that contains 2 rows with random 2 elements from 0 to 99
random_2_D=random.randint(100, size=(2,1,2))
print(random_2_D)


# generating an integer random 2-D array that contains 2 rows with random 2 elements from 0 to 99
print(" generating an integer random 2-D array that " 
"contains 2 rows with random 2 elements from 0 to 99")
r_f_dd=random.rand(2,3)
print(r_f_dd)


# !!!!!!!!!!!!!!!!!!!  generating random number from a given array  !!!!!!!!!!!!!!!!!!!!
arr=np.array([2,3,4,66,1,88,90,1])
random_from_array=random.choice(arr)
print(random_from_array)


# ---------------------------  generate a new array that contain randomly selected elements
#                               from previous array
from numpy import random
import numpy as np
rand=np.array([3,5,7,9])
d=random.choice(rand, size=(5))
print(d)


# create a 2-D array from 1-D array and the elements in 2-D are actually randomly selected
# elements from 1-D
d=np.array([1,2,3,4,5,6])
random_num_from_d=random.choice(d)
dd=random.randint(random_num_from_d, size=((2,2)))
print(dd)


# CONCLUSION:
print()
print()
print()
print(random.randint(100, size = (2,2)))
print(random.rand(3,2,1))

print(random.choice(random.randint(100,200,size = 5), (2,2) ))
