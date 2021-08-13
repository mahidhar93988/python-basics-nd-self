# difference_sum_even_odd_index
# You should name your function as difference_sum_even_odd_index
# It should take a list of integers
# Return an integer

def difference_sum_even_odd_index(arr):
    e = 0
    o = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            e += arr[i]
        else:
            o += arr[i]

    return e-o


# Do not change anything below this line
if __name__ == "__main__":
    numbers = [int(i) for i in input().split(' ')]
    print(difference_sum_even_odd_index(numbers))
