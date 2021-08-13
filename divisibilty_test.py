# divisibilty test

def divisibility(arr, n, x):
    result = 0

    for i in arr:
        if i % x == 0:
            result += 1

    return result


n, x = map(int, input().split())
arr = [int(x) for x in input().split()]
print(divisibility(arr, n, x))
