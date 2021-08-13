# counting_odd_even_numbers

N = int(input())

i = 0
o = 0
e = 0
while (i<N):
    n = int(input())
    if (n%2==0):
        e+=1
    else:
        o+=1
    i+=1
print("no.of odds:", o)
print("no.of evens:", e)   
