# your code goes here
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
sum = 0
min = 9999999
for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]
for digit in str(min):
    sum += int(digit)
if sum % 2 == 0:
    print(1)
else:
    print(0)
