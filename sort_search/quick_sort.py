
def quick_sort(arr, first, last):
    if first < last:
        pivot_i = partition(arr, first, last)
        quick_sort(arr, first, pivot_i - 1)
        quick_sort(arr, pivot_i + 1, last)
    return arr

def partition(arr, first, last):
    pivot_i = first
    pivot = arr[first]

    while first < last:
        while first < len(arr) and  arr[first] <= pivot:
            first += 1
        
        while arr[last] > pivot:
            last -= 1
        
        if first < last:
            swap(arr, first, last)

    swap(arr, last, pivot_i)
    return last

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

A = [30, 40, 20, 15, 32]
print(A)
print(quick_sort(A, 0, len(A)-1))

print(A)