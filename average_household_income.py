# average house hold income

N = int(input())
inc = []
pop = []
for i in range(N):
    inc.append(int(input()))
for i in range(N):
    pop.append(int(input()))

add = 0
count = 0
for i in range(N):
    if(pop[i] > 2):
        count += 1
        add += inc[i]
if(count == 0):
    print("-1")
else:
    print(add//count)
