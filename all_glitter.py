
N = int(input())
price1 = [int(i) for i in input().split()]
price2 = [int(j) for j in input().split()]

# lucy
for all in ([i], [j]):
    if price1[i] <= price2[j]:
        print("Lucy")
    elif quality[i] >= quality[j]:
        print("Mark")
    else:
        print("none")
