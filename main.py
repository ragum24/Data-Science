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

array_4 = np.arange(20).reshape(10,2) 
print(array_4)

#by without using reshape, the array become a 1D array, while when you 
#use factors of that number it becomes an 2D array

#generate 10 random numbers and create an array

rand_num = np.random.randint(0,56)
print(rand_num)
rand_array = np.random.randint(20,80,10) #parameters: lowest, highest, how many numbers
print(rand_array)

max_num = rand_array.max()
print(f"Biggest number: {max_num}")

minnie_mouse = rand_array.min()
print(f"Smallest number: {minnie_mouse}")

#generating random 2D array
rand_2D = rand_array.reshape(5,2)

#asending order
print(f"Sorting a 1D array: {np.sort(rand_array)}")
print(f"Sorting row-wise: {np.sort(rand_2D,axis=1)}") #axis represents the rows and columns

