

N = int(input())

zero = 0
one = 0
two = 0
for _ in range(N):
    temp = int(input())
    if (temp == 0):
        zero += 1
    elif(temp == 1):
        one += 1
    else:
        two += 1

while(zero):
    print(0)
    zero -= 1
while(one):
    print(1)
    one -= 1
while(two):
    print(2)
    two -= 1
