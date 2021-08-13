M = int(input())
N = int(input())

A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

max_a = 0
max_b = 0
for i in A:
    max_a = max(max_a, max(i, -i))
for i in B:
    max_b = max(max_b, max(i, -i))
print(max_a*max_b)
