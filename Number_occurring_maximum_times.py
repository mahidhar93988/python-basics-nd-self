# Number_occurring_maximum_times

def solve(arr, n):

    count = 1

    for i in range(1, n):
        if arr[i] == arr[i-1]:
            count += 1

        else:
            if count == 4:
                return arr[i-1]
            count = 1

    if count == 4:
        return arr[n-1]

    return -1


n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

print(solve(arr, n))
