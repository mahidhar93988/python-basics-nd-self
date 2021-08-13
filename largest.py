# largest
def largestElement(A):
    # Code here
    largest = A[0]
    for i in range(n):
        if A[i] > largest:
            largest = A[i]
    return largest


n = int(input())
A = [int(x) for x in input().split()]
print(largestElement(A))
