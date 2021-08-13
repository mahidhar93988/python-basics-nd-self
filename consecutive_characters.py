# consecutive characters

string = input()
if(len(string) == 0):
    print(0)
else:
    maxm = 1
    count = 1
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count += 1
            maxm = max(maxm, count)
            continue
        count = 1
    print(maxm)
