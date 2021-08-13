n = int(input())
list1 = []
for i in range(n):
    element = input()
    list1.append(element)


bulb = "OFF"
Count = 0
for i in range(n):
    if(list1[i] == "ON"):
        if(bulb == "OFF"):
            bulb = "ON"
            Count += 1
        else:
            continue
    elif(list1[i] == "OFF"):
        if(bulb == "ON"):
            bulb = "OFF"
        else:
            continue
        # toggle condition
    else:
        if(bulb == "OFF"):
            bulb = "ON"
            Count += 1
        else:
            bulb = "OFF"
print(Count)
