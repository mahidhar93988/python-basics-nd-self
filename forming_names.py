# forming names

n = int(input())
sub_string = input()
list = list(map(str, input().split()))
possible = True
for i in sub_string:
    if i in list:
        continue
    else:
        possible = False
if possible == True:
    print("true")
else:
    print("false")
