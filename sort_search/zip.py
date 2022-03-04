
def zip_a_to_b(a, b):
    i = len(a)-len(b)-1
    j = len(b)-1
    print(i)
    while i >= 0 and j >=0:
        if a[i] > b[j]:
            a[i+j+1] = a[i]
            i += -1
            print(a)
        else:
            a[i+j+1] = b[j]
            j += -1
            print(a)
    while j >= 0:
        a[j] = b[j]
        j -= 1
    return(a)


B = [2,4,8,11,37]
A = [0,0,1,1] + [0]*len(B)

print(zip_a_to_b(A,B))

#O(A+B)