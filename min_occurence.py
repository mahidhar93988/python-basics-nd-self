N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

res = 0
for i in range(len(arr)):
    res = res ^ arr[i]

print(res)

