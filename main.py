import numpy as np

my_list = [1,5,8,4,3,8,80]
my_array = np.array(my_list)

print(my_list)
print(my_array)

#adding
list_add = my_list + my_list  #this is list repetition
array_add = my_array + my_array  #element-wise addition
print(list_add)
print(array_add)

#multiplication
print(my_list * 2)
print(my_array * 2)

all_0 = np.zeros((3,5))
print(all_0)

all_1 = np.ones((4,8))
print(all_1)

array_1 = np.arange(20)
print(array_1)

array_2 = np.arange(18).reshape(3,6)
print(array_2)

array_3 = np.arange(18).reshape(2,9)
print(array_3)