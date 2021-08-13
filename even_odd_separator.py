# even odd separator
#  Write a function with name even_odd_separator, you should exactly the same name
# This even_odd_separator functions should take a list of integers and return a list
# you can start from here

def even_odd_separator(arr):
    odd = []
    even = []

    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return odd+even


# Do not change anything below this line
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    separated = even_odd_separator(numbers)
    for num in separated:
        print(num)
