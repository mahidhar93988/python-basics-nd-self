def replaceElements(arr):
    # Implement this function
    prev_max = arr[-1]
    arr[-1] = -1
    i = len(arr)-2
    while(i >= 0):
        curr = arr[i]
        arr[i] = prev_max
        prev_max = max(prev_max, curr)
        i -= 1
    return(arr)


# Do not edit anything below
if __name__ == "__main__":
    num_elems = int(input())
    arr = []
    for index in range(num_elems):
        arr.append(int(input()))

    for elem in replaceElements(arr):
        print(elem)
