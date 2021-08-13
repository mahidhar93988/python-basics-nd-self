# macbook
n = int(input())
count = 0
for i in range(n):
    number = int(input())
    if (number <= 0):
        continue
    else:
        count += number

print(count)
