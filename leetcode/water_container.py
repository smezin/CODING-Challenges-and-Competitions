class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            water = max(water, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        print(water)
        return water

s = Solution()
height = [1,8,6,2,5,4,8,25,7]
#print(s.get_best_right(height))
s.maxArea(height)