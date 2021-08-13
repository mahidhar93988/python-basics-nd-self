# clock

in1 = input()
in1 = in1.split()
m, n = in1
m, n = int(m), int(n)
add = m+n
if (add % 12 == 0):
    print(12)
else:
    print(add % 12)
