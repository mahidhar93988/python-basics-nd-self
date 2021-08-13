# mean

n = int(input())

arr = [int(x) for x in input().split()]

s = 0
for i in arr:
    s += i

print(s//n)
