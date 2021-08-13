# your code goes here
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

maxm = -999999999999999
for i in range(N-1):
    if(arr[i]*arr[i+1] > maxm):
        maxm = arr[i]*arr[i+1]

print(maxm)
