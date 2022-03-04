
import re


def bin_search_rotated(arr, n, index=0):
    middle = len(arr) // 2
    if len(arr) == 1:
        if arr[0] == n:
            return index
        else:
            return False
    if arr[middle] == n:
        return middle + index

    if arr[0] < arr[middle]: #left side sorted
        if n < arr[middle]:
            return bin_search_rotated(arr[:middle], n, index)
        else:
            return bin_search_rotated(arr[middle:], n, middle + index)
    if arr[middle] < arr[len(arr)-1]: #right side sorted
        print('==')
        if n < arr[middle]:
            return bin_search_rotated(arr[:middle], n, index)
        else:
            return bin_search_rotated(arr[middle:], n, middle + index)
    else: #at least on side is all eqauls
        if arr[0] == arr[middle]:
            if arr[middle] != arr[len(arr)-1]:
                return bin_search_rotated(arr[middle:], n, middle + index)
            else:
                res = bin_search_rotated(arr[:middle], n, index)
                if not res:
                    return bin_search_rotated(arr[middle:], n, middle + index)
                else:
                    return res

A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
S = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]
R = [2, 2, 2, 3, 4, 2]

#for i in R:
print(f'found {4} in index {bin_search_rotated(R, 4)}')

