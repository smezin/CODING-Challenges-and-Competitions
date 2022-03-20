def all_perms_generator(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield (perm[:i] + elements[0:1] + perm[i:])

def all_perms(nums):
    if len(nums) <= 1:
        return nums
    i = len(nums) - 2
    while i > 0 and nums[i] > nums[i+1]:
        i -= 1
    print(i)
    if i > 0:
        last = len(nums) - 1
        while nums[last] < nums[i]:
            last -= 1
        print('--',nums[i], nums[last])
        swap(nums, i, last)
        head = nums[0:i+1]
        tail = nums[i+1:]
        print (tail)
        tail = tail[::-1]
        return head + tail
    return nums[::-1]
    


def swap(arr, i, j):
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]

input0 = [1,5,8,4,7,6,5,3,1]
input1= [3,2,1]
g = all_perms(input1)
print(g)