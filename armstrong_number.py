# Armstrong Number

n = int(input())
sum = 0
power = len(str(n))
count = n
while(n > 0):
    digit = n % 10
    sum += digit**power              # 153 = 1^3 + 5^3 + 3^3
    n = n//10

if (sum == count):
    print("Yes")
else:
    print("No")
