# input_reader
class input_reader:
    def __init__(self):
        self.data = []

    def read_strings(self, N):
        while(N > 0):
            self.data.append(input())
            N -= 1

    def read_integers(self, N):
        while(N > 0):
            self.data.append(int(input()))
            N -= 1

    def read_float(self, N):
        while(N > 0):
            self.data.append(round(float(input()), 2))
            N -= 1


N = int(input())
ins = input()
temp = input_reader()
if(ins == "strings"):
    temp.read_strings(N)
if(ins == "integers"):
    temp.read_integers(N)
if(ins == "float"):
    temp.read_float(N)
for i in range(len(temp.data)):

    print(i, temp.data[i])
