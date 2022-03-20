def threeSum(nums):
    res = []
    for i in range(len(nums)-2):
        if i == 0 or nums[i] != nums[i-1]:
            res += twoSum(nums, i)
    return res

def twoSum(nums, pivot):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    res = []
    nums.sort()
    smallest = pivot + 1
    biggest = len(nums) - 1
    while smallest < biggest:
        if nums[pivot] + nums[smallest] + nums[biggest] > 0:
            biggest -= 1
        elif nums[pivot] + nums[smallest] + nums[biggest] < 0:
            smallest += 1
        else:
            res.append([nums[pivot], nums[smallest], nums[biggest]])
            smallest += 1   
            biggest -= 1
            while smallest < biggest and nums[smallest] == nums[smallest - 1]:
                smallest += 1
            while smallest < biggest and nums[biggest] == nums[biggest + 1]:
                biggest -= 1
            
    return res

input = [-1,0,1,2,-1,-4,]
print(threeSum(input))