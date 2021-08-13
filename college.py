# college
# sum of divisors of given number

def sumofdivisors(n):
    # Code here
    divisors = [1]

    for i in range(2, n+1):
        if (n % i) == 0:
            divisors.append(i)
    return t(divisors)


n = int(input())
print(sumofdivisors(n))
