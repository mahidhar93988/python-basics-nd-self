inc = 1
dec = 1
N = int(input())
arr = []
i = 0
while(i < N):
    arr.append(int(input()))
    i += 1

for i in range(len(arr)-1):
    if(arr[i] < arr[i+1]):
        dec = 0
    if (arr[i] > arr[i-1]):
        inc = 0
if (inc == 1 or dec == 1):
    print("True")
else:
    print("false")
