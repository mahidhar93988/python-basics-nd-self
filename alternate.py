# your code goes here

arr = [int(x) for x in input().split()]

sum1, sum2 = 0, 0

for i in range(9):
    if i % 2 == 0:
        sum1 += arr[i]
    else:
        sum2 += arr[i]

print(sum1)
print(sum2)
