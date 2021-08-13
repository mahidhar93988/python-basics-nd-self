# # Given two numbers add both of them return the result.

# def add_two_numbers(a, b):
#     sum = a + b
#     return sum

# # Big O notation..
# # O(1) , O(n)....
# # c1 => O(c1) => O(1)..

def multiply_two_numbers(a, b):
    product = a * b 
    return product


# Given a list or array find the sum of all the elements in the array.
# without internal definition functions..
# arr  = [1, 2 ,3 ,4, 5] -> n

def sum_of_array(arr):
    sum = 0
    
    for i in range(len(arr)): # 7 ..is this const ? n 
        sum = sum + arr[i]
    return sum

# sum(arr) # O(n) 
# O(1)

# c1 -> means constant..
# L22 c1 + L24 (c2 * n) + (c3 * n) + c4

# is O(n) the highest ??
# O(1) + O(n) => O(n)

# O(n) =>

# O(1) + L24 O(n) + L25 O(n) + O(1)
# O(2 * n) => # O(n) # generally we drop the contants..


# Find min and max in an array .. 

def find_min_max(arr):
    min = 10000
    max = -10000
    for i in range(len(arr)): # n
        if (arr[i] < min):
            min = arr[i] # c1
        
        if (arr[i] > max):
            max = arr[i] # c2.

# (c1 * n) + (c2 * n)
# O(n) + O(n) => O(2*n) =>O(n)

arr = [-1, 2, 3, 5, 10, -2, 4, 5, 6, 19 , 9, 0] -> # size n..

def find_min_max_2(arr):
    # time library..
    # start = time.start()
    min = 10000 
    max = -10000
    externalArr = []

    for i in range(len(arr)): # n
        if (arr[i] < min):
            min = arr[i] # c1
    
    for i in range(len(arr)): # n
        if (arr[i] > max):
            max = arr[i] # c2

    for i in range(len(arr)):
        externalArr[i] = arr[i] # O(n..)
    # print(time.end() - start)

# 1 + 1 + 1 + ........ n times... => n
# 4 + 4 => 8 btyes..?
# (c1 * n) + (c2 * n)
# O(n) + O(n) => O(2*n) => O(1) < O(n) < O(n * n)

# O(n) or O(n + 1)

# Time complexity -> O(1), O(n), O(n^2), O(n^3), O(logn), O(n^n), O(nlogn)

# Space complexity ..
# Input space complexity -> O(n)...
# Extra space complexity  -> O(1), O(n)



def return_static_array(n):
    arr = [1,2,3,3,4,5,6,7,8] #...O(1..)
    return arr


# some more problems.. try deduce the time complexity of those..
# given inputs m and n print matrix pattern with *

def print_pairs(arrA, arrB):
    for i in range(len(arrA)):
        for j in range(len(arrB)):
            for k in range(100000):
                print (arrA[i] + '---' + arrB[j])

# Inplace reversing an array is a good one..

# Next classes let's look at recursion O(2^n), 
# may be binary search.. O(logn) for O(logn) Inplace 

