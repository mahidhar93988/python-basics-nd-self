
def matchMaker(G, B, N):
    G.sort()
    B.sort(reverse=True)

    res = 0

    for i in range(N):
        if G[i] % B[i] == 0 or B[i] % G[i] == 0:
            res += 1

    return res


for i in range(int(input())):
    n = int(input())
    girls = [int(x) for x in input().split()]
    boys = [int(x) for x in input().split()]
    print(matchMaker(girls, boys, n))
