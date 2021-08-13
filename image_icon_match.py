# image icon match
N = int(input())
image = []
for i in range(N):
    image.append(int(input()))
m = int(input())
icon = []
for i in range(m):
    icon.append(int(input()))

if (m == 0):
    print(0)
else:
    count = 0
    for i in range(N-m+1):
        window = image[i:i+m]
        if(window == icon):
            count += 1
    print(count)
