# your code goes here
class HopRacing:
    def __init__(self):
        self.hops = 0
        self.rounds = 0

    def getRounds(self, value):
        self.hops += value

        if self.hops <= 10:
            self.rounds += 1
        return self.rounds


h1 = HopRacing()
h2 = HopRacing()

for i in range(int(input())):
    a, b = map(int, input().split())
    if a == 1:
        h1.getRounds(b)
    elif a == 2:
        h2.getRounds(b)

if h2.rounds < h1.rounds:
    print(2)
else:
    print(1)
