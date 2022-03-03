def merge_sort(array):
    helper = []
    left = 0
    right = len(array)-1
    merge_sort_divide(array, helper, left, right)

def merge_sort_divide(array, helper, left, right):
    if left < right:
        middle = (right+left)//2
        merge_sort_divide(array, array[:middle], left, middle)
        merge_sort_divide(array, array[middle:], middle+1, right)
        print('merge->',array,'left:', left, 'right:', right, 'middle:', middle)
        merge(array, helper, left, right, middle)

def merge(array, helper, left, right, middle):
    #helper = array[:]
    h_left = left
    h_right = middle+1
    current = left
    while h_left <= middle and h_right <= right: 
        if helper[h_left] < helper[h_right]:
            array[current] = helper[h_left]
            h_left += 1
        else:
            array[current] = helper[h_right]
            h_right += 1
        current +=1
    remaining = middle - h_left
    print('remaining:',helper[h_left:h_left+remaining+1])
    array[current:current+remaining+1] = helper[h_left:h_left+remaining+1]

a = [2,6,5,1,3,0,4]
merge_sort(a)
print(a)