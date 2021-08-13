# finding prime number

N = int(input())
i = 0
while (i < N):
    n = int(input())
    if (n == 1):
        print("NO")
        i += 1  # i = i+1
        continue
    j = 2
    ind = 0
    while(j <= n-1):
        if (n % j == 0):
            ind = 1
        j += 1
    if(ind == 0):
        print("Yes")
    else:
        print("No")
    i += 1

    # nd
