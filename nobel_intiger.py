# Nobel intiger
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
ind = -1
for P in arr:
    count = 0
    for num in arr:
        if(num > P):
            count += 1
    if (count == P):
        ind = 1
        break
print(ind)
