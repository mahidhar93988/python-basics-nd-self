# Count occurence

N = int(input())
i = 0
arr = []
while(i < N):
    arr.append(int(input()))
    i += 1
q = int(input())

count = 0
for i in arr:
    if(i == q):
        count += 1
print(count)

# nd
