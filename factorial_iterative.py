# factorial iterative

num = int(input())


def recur_factorial(n):
    if (n == 1 or n == 0):
        return 1
    elif n < 1:
        return ("undefined")
    else:
        return n*recur_factorial(n-1)


print(recur_factorial(int(num)))
