def solve(matrix):
    N = len(matrix)
    M = len(matrix[0])
    sum = [[0 for i in range(M+1)]
           for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):

            sum[i][j] = (max(sum[i-1][j],
                             sum[i][j-1]) +
                         matrix[i-1][j-1])
    return sum[N][M]


# Do not modify anything below this line
M, N = [int(i) for i in input().split()]
matrix = []
for i in range(M):
    row = [int(i) for i in input().split()]
    matrix.append(row)
print(solve(matrix))
