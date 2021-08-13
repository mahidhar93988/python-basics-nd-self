# frequency_101
def freq(arr, n, k):
    count = 0

    for i in arr:
        if i == k:
            count += 1

    return count


n, k = map(int, input().split())

arr = list(map(int, input().split()))
print(freq(arr, n, k))
