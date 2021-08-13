# Eating symbols
R = input()
brain = 0
for i in R:
    if(i == '-'):
        brain -= 1
    else:
        brain += 1
print(brain)
