# your code goes here

n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
res = 0
for i in range(0, 2*n, 2):
    res += arr[i]

print(res)
