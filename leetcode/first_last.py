from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
            
        def bs(left, right, target):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if right-left <= 1:
                return -1
            elif nums[mid] > target:
                return bs(left, mid, target)
            elif nums[mid] < target:
                return bs(mid, right, target)
            
        
        idx = bs(0, len(nums), target)
        if idx == -1:
            return [-1, -1]
        start, end = idx, idx
        while start >= 0 and nums[start] == target:
            start -= 1
        start += 1
        while end < len(nums) and nums[end] == target:
            end += 1
        end -= 1
        return [start, end]

I = [0]
s = Solution()
res = s.searchRange(I, 1)
print(res)