# predict the seat

N = int(input())
i = 0
while (i < N):
    c, b = [int(i) for i in input().split()]
    if (b > c or b <= 0):
        print("Invalid")
        i += 1
        continue
    if (b % 8 == 1 or b % 8 == 4):
        print("L")
    elif(b % 8 == 2 or b % 8 == 5):
        print("M")
    elif(b % 8 == 3 or b % 8 == 6):
        print("U")
    elif(b % 8 == 7):
        print("SL")
    else:
        print("SU")
