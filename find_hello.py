N = int(input())
arr = []
for i in range(N):
    arr.append(input())

for word in arr:
    ind = 0
    for j in range(len(word)-len("hello")+1):
        if(word[j:j+5] == "hello"):
            ind = 1
            break
    if (ind == 1):
        print("Yes")
    else:
        print("No")
