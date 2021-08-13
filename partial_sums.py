# partial sums

n, k = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
add = 0
for i in arr:
    add += i
ind = 0
for i in arr:
    if(add-i) == k:
        ind = 1
        break
if(ind == 0):
    print(0)
else:
    print(1)
