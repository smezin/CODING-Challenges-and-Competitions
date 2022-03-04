def bin_search(n, arr, index=0):
    middle = len(arr)//2
    if len(arr) == 1:
        if arr[0] == n:
            return index
        else:
            return False
    if n == arr[middle]:
        return middle+index
    if n < arr[middle]:
        return bin_search(n, arr[:middle], index)
    else:
        return bin_search(n, arr[middle:], index+middle)

#print(bin_search(30, [10,20,30,40,50]))
S = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]

for i in S:
    print(f'found {i} in index {bin_search(i, S)}')
    