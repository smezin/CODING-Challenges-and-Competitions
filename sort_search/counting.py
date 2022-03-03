
# Python program for counting sort
  
# The main function that sort the given string arr[] in 
# alphabetical order

def countSort(arr):
  
    # The output character array that will have sorted arr
    output = [' ' for i in range(len(arr))]
  
    # Create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for i in range(256)]
  
    # For storing the resulting answer since the 
    # string is immutable
    ans = ["" for _ in arr]
  
    # Store count of each character
    for i in arr:
        count[ord(i)] += 1
    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i-1]

    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
        #print(output)
  
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans 
  
# Driver program to test above function
arr = "009901188854"
ans = countSort(arr)
print("Sorted character array is % s" %("".join(ans)))


def countingsort(lst):
   
    count_size = max(lst)
    
    output = lst[:]
    count = [0] * count_size
  
    for i in range(0, len(lst)):
        count[lst[i]-1] += 1

    for i in range(1, count_size):
        count[i] += count[i-1]

    for i in range(len(lst)-1, -1, -1):
        output[count[lst[i]-1]-1] = lst[i]
        count[lst[i]-1] -= 1
    return output

lst = [38, 378, 985, 902, 7914, 981, 765, 770, 45, 313, 907, 400, 50, 196, 5, 96]
result = countingsort(lst)
print("original list: ",lst)
print('counting sorted list: ',result)