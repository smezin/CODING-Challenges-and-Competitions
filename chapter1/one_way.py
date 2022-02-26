
def is_replaced (a, b):
    dif = 0
    if len(a) == len(b):    
        for i in range (len(a)):
            if a[i] != b[i]:
                dif += 1
                if dif > 1:
                    print (f'{a} and {b} -> replaced: {dif}')
                    return False

    print (f'{a} and {b} -> replaced: {dif}')
    return True

def is_insert_delete(a, b):
    dif = 0
    if len(a) == len(b) + 1:
        _long = a
        _short = b
        n = len(a)
    elif len(a) + 1 == len(b):
        _long = b
        _short = a
        n = len(b)
    else:
        return False
   
    for i in range(n):
        print(i, dif, _long[i],_short[i-dif])
        if _long[i] != _short[i-dif]:
            dif += 1
            if dif > 1:
                print(f'{a} and {b} -> added/removed {dif}')
                return False
            if i == n-1:
                dif += 1
    print(f'{a} and {b} -> added/removed {dif}')
    return True

# is_replaced('abcd', 'abcd')
# is_replaced('Xbcd', 'aXcd')
# is_replaced('abcd', 'abcX')
# is_replaced('abXd', 'abcd')
# is_insert_delete('Xabcd', 'abcd')
is_insert_delete('abcd', 'abcdX')
# is_insert_delete('abd', 'abcd')
# is_insert_delete('abcd', 'abc')

# Python program to check if given two strings are
# at distance one
 
# Returns true if edit distance between s1 and s2 is
# one, else false
def isEditDistanceOne(s1, s2):
 
    # Find lengths of given strings
    m = len(s1)
    n = len(s2)
 
    # If difference between lengths is more than 1,
    # then strings can't be at one distance
    if abs(m - n) > 1:
        return False
 
    count = 0    # Count of isEditDistanceOne
 
    i = 0
    j = 0
    while i < m and j < n:
        # If current characters dont match
        if s1[i] != s2[j]:
            if count == 1:
                return False
 
            # If length of one string is
            # more, then only possible edit
            # is to remove a character
            if m > n:
                i+=1
            elif m < n:
                j+=1
            else:    # If lengths of both strings is same
                i+=1
                j+=1
 
            # Increment count of edits
            count+=1
 
        else:    # if current characters match
            i+=1
            j+=1
 
    # if last character is extra in any string
    if i < m or j < n:
        count+=1
 
    return count == 1
 
# Driver program
s1 = "gfg"
s2 = "gf"
if isEditDistanceOne(s1, s2):
    print ("Yes")
else:
    print ("No")
 