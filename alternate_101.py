# alternate_101

n = int(input())
l = list(map(int, input().split()))
i = 0
res = 0
while(i < n):
    res += l[i]
    i += 2

print(res)
