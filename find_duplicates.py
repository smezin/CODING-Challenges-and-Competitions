

def find_dups(array1, array2):
    i = 0 
    count=0
    j=0
    while True:
        if array1[i] < array2[j]:
            i += 1
        elif array1[i] > array2[j]:
            j += 1
        else:
            print(array1[i])
            count += 1
            i += 1
        if i >= len(array1) or j >= len(array2):
            break
    return count

A = [2,4,7,11,43,55,66,91]
B = [4,7,22,55,66,72,90,91]

find_dups(A,B)

#Errors:
# Did not initialize count
# Broke of 'and' instead of if
#




        
