import numpy as np

array1 = np.random.randint(0,19,20)

print(f"The array: {array1}")

print(f"First 5 elements: {array1[0:5]}")

print(f"Last 5 elements: {array1[-5::]}")
#-5 is the starting, becasue it will jump from 0 to the 5th
#last index position in the array 
#if the array's step is +1, there is no need to give it a step,
#as this is default

print(f"Every 3rd element: {array1[0:20:3]}")

print(f"In reverse order: {array1[::-1]}") 
#the 2 sections are empty because the default starting pos will be at 
# index 0, while default ending pos will be at the end of the array. 
# -1 is the number of steps, meaning that it will be reversed
