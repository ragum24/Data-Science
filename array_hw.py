import numpy as np

# matrix is another word for array  :)

matrix1 = np.arange(9,18).reshape(3,3)
matrix2 = np.arange(6,15).reshape(3,3)

#start stop step are the parametres for the function arange
#for this, the step is not compulsory so, only the starting and ending (start,stop) are really needed
#the numbers in arange (the start, between and the end) all have to match with the number of digits required to reshape it


print(f"Matrix 1: \n{matrix1}\n")

print(f"Matrix 2: \n{matrix2}\n")

# Element-wise multiplication
element_wise = matrix1*matrix2
print(f"\nElement-wise multiplication: \n{element_wise}\n")


#element-wise multiplication is where each element from a matrix and its corresponding element from the other matrix multiply with each other

# Matrix multiplication
# @ = matmul = matrix multiplication

matrix_multiplication = matrix1 @ matrix2
print(f"\nMatrix multiplication: \n{matrix_multiplication}\n")

#matrix multiplication:

#matrix1 :
# [[9 10]
# [11 12]]

#matrix2 :
# [[6 7]
# [8 9]]

#to calculate, each row in the first matrix multiplies to each column in the second matrix and the results get added

# e.g. 9x6 + 10x8 = 134
# 9x7 + 10x9 = 153
# 11x6 + 12x8 = 162
# 11x7 + 12x9 = 185

# [[134 153]
# [162 185]]