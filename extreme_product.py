# extreme product
n = int(input())
list1 = []
for i in range(n):
    element = int(input())
    list1.append(element)

smallest = min(list1)
largest = max(list1)

# print(f"numbers is {largest}")
# print(f"numbers is {smallest}")

smallest = int(smallest)
largest = int(largest)

addition = smallest * largest

print(addition)

# output is 50% not completed
