def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    mapped = {}
    for i in range(len(nums)):
        mapped[nums[i]] = i
    print(mapped)
    res = []
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in mapped and mapped[complement] != i:
            res.append([i, mapped[complement]])
    return res
def twoSum1(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
       
        nums.sort()
        smallest = 0
        biggest = len(nums) - 1
        while smallest < biggest:
            if nums[smallest] + nums[biggest] > target:
                biggest -= 1
            elif nums[smallest] + nums[biggest] < target:
                smallest += 1
            else:
                res.append([nums[smallest], nums[biggest]])
                smallest += 1
                biggest -= 1
                while smallest < biggest and nums[smallest] == nums[smallest - 1]:
                    smallest += 1
               
        return res
            
input = [-1,0,1,2,-1,1,-2]
print(twoSum1(input, 0))
input.sort()
#print (input)