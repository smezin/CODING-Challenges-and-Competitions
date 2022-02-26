def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        print(f'calling left with {L}')
        mergeSort(L)
  
        # Sorting the second half.
        print(f'calling right with {R}')
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            print(arr)
  
        # Checking if any element was left
        while i < len(L):
            print(f'L={L} picked')
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            print(f'R={R} picked')
            arr[k] = R[j]
            j += 1
            k += 1
  
# Code to print the list
  
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
  
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 70]
    #print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    #print("Sorted array is: ", end="\n")
    printList(arr)