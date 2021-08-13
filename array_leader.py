
def leader(A, N):
    res = []
    maxx = float('-inf')
    for i in range(N-1, -1, -1):
        maxx = max(maxx, A[i])
        if A[i] == maxx:
            res.append(A[i])

    return res


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

for i in leader(arr, n):
    print(i)
