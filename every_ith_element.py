# every I th element

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
I = int(input())
add = 0
for ind in range(len(arr)):
    if ((ind+1) % I == 0):
        add += arr[ind]
print(add)
