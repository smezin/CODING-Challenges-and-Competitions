
def radix(array):
    max_num = max(array)
    i = 1
    while max_num // 10**(i-1) > 0:
        array = count_sort_ints(array, i)
        i += 1
    print(array)


def count_sort_ints(array, by_digit):
    n = len(array)
    output = [0] * n
    count = [0] * 10

    for j in array:
        count[d(j, by_digit)] += 1

    for i in range(1,10):
        count[i] += count[i-1]
    
    for k in range(len(array)-1, -1, -1):
        output[count[d(array[k], by_digit)]-1] = array[k]
        count[d(array[k], by_digit)] -= 1
    
    array = output[:]
    return array

def d (num, digit):
    d = num//10**(digit-1)
    return d%10

array = [38, 1378, 985, 902, 7914, 981, 765, 770, 45, 313, 907, 400, 50, 196, 5, 96]
print(array)
radix(array)
