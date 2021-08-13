
# your code goes here

def calculateF(n):
    n1 = n//2
    n2 = n-n1

    sum1 = n1*(n1+1)
    sum2 = n2**2

    return sum1-sum2


n = int(input())
print(calculateF(n))
