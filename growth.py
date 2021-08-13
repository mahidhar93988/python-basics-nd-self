n = int(input())
list = []
for i in range(n):
    element = int(input())
    list.append(element)

add = 0
for i in range(0, len(list)):
    add = add + list[i]

ave = add / n

if ave > 100:
    print("Excellent!")
else:
    print("Not Excellent!")
