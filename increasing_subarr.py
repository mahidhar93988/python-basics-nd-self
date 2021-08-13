

def increasingSubarr(A, n):
    length = 1
    count = 1
    end = 1

    for i in range(1, n):
        if A[i] > A[i-1]:
            count += 1
        else:
            if count > length:
                length = count
                end = 1
            count = 1

    if count >= length:
        length = count
        end = n

    return[length, end-length+1, end]


n = int(input())
arr = [int(x) for x in input().split()]
print(*increasingSubarr(arr,n))
