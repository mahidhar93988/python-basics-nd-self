# matrix_101

def matrix(arr, n, m):

    add = 0

    for i in range(n):
        for j in range(m):

            add += (arr[i][j] if arr[i][j] % 2 != 0 else 0)

    return add


n, m = map(int, input().split())

arr = [[int(x) for x in input().split()] for i in range(n)]

print(matrix(arr, n, m))
