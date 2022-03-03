def bin_search(n, arr):
    print('called:', arr)
    middle = len(arr)//2
    if len(arr) == 1:
        if arr[0] == n:
            return True
        else:
            return False
    print(middle, arr[middle])
    if n == arr[middle]:
        return True
    if n < arr[middle]:
        return bin_search(n, arr[:middle])
    else:
        return bin_search(n, arr[middle:])

print(bin_search(40, [10,20,30,40,50]))

    