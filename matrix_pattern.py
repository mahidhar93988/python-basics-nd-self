# given n are two integers., you have to print * in matrix pattern format
# 
# 4
# 
# * * * *
# * * * * 
# * * * * 
# * * * * 

# 3, 3

# * * *
# * * *
# * * *

def print_matrix_pattern(n):
    for i in range(m): # n = 6 
        for i in range(n): # n
            print('* ', end='')
        print('')

print_matrix_pattern(4)

# 1 , n
# 2, n
# 3, n 
# 4, n....

# 1, 6
# 2, 6
# 3, 6 
# .... 6 tjmes

# n, n

# n + n + n ...... n tom,es

# n * n.. = n^2..
# 3 nested for loops -> O(n * n * n) = n^3..

# n * (n)