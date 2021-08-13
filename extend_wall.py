# your code goes here

N = int(input())
arr = [int(i) for i in input().split()]
num = 0
total = 0
for i in range(1, len(arr)):
    if arr[i] <= arr[i-1]:
        num = arr[i-1]+1-arr[i]
        arr[i] = arr[i]+num
        total += num
print(total)
