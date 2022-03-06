
def bin_search(arr, n):
    """
    param arr: Sorted list of comparable items
    param n: Item to be found
    returned value: index of item if found, None otherwise
    """
    first = 0
    last = len(arr) - 1
    return bin_search_rec(arr, first, last, n)

def bin_search_rec(arr, first, last, n):
    #print(arr, first, last, n)
    middle = (first + last) // 2
    if arr[middle] == n:
        return middle
    if n > arr[middle]:
        return bin_search_rec(arr, middle+1, last, n)
    else:
        return bin_search_rec(arr, first, middle-1, n)

def find_size(arr):
    return find_size_rec(arr, 0, 1)

def find_size_rec(arr, greatest_known, count):
    """
    param arr: List of unknown size, with disabled 'len' method. arr[i] returns -1 if i is out of range
    param greatest_known: greatest known index that contains an item
    """
    greatest_runner = greatest_known
    if get_by_index(arr, greatest_known+1) == -1:
        return greatest_known, count
    
    i = -1
    while get_by_index(arr, greatest_runner) != -1:
        i += 1
        greatest_runner = greatest_known + 2**i
    return find_size_rec(arr, greatest_known + 2**(i-1), count+1)

def get_by_index(arr, index):
    try:
        return arr[index]
    except:
        return -1

def get_by_index_int(arr, index):
    if index < arr:
        return index
    else:
        return -1

