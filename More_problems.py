# some more problems.. try deduce the time complexity of those..
# given inputs m and n print matrix pattern with *

# 3 , 2
# * *
# * *
# * *

def print_matrix_pattern_just_print(m, n):
    for i in range(m):
        for j in range(n):
            print('*', end=' ')
        
        print('')
# space complexity = O(1)
# Time complexity = O(m * n)


# int # 8 Bytes....(-2^32 to 2^32) and string.. storage.. , 
# ['****', ****, ****, ****, ****, ****, ****, ****, ****, ****,  ] 
# 
def print_matrix_pattern(m, n):
    storage = []
    array_defalut = [1] # O(1)
    for i in range(m):
        pattern = ''
        for j in range(n):
            pattern = pattern + '*'
        storage.append(pattern) # O(m)
    
    print(storage)
# space complexity = O(m) -> O(m * n)
# Time complexity = O(m * n)
    
print_matrix_pattern(4, 4)
# m * n => O(m * n) -> Time com
# => O(1).. -> Space..





############## 
# size of arrA and arrB is n.. 10 , 20, n.. 
def print_pairs(arrA, arrB):
    for i in range(len(arrA)): # O(n)
        for j in range(len(arrB)): # O(n) => O(n * n)
            for k in range(100000): # O(100000) => O(100000 * n * n) => O(n * n)
                print (arrA[i] + '---' + arrB[j])

# space complexity = O(1) .., O(n^3)..
# Time complexity = O(n^3) , O(n^2)... 


# space complexity = O(1).. 
# Time complexity = O(100000 * n * n) => O(n^2)..
# O(1) < O(logn) < O(n) < O(n^2)...

# O(100000 * n * n) > O(n^2)


#### 
