class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        good_indexes = [False] * n
        good_indexes[n-1] = True
        index_changed = True
        i = n - 1
        while i > 0:
            if good_indexes[i]:
                for j in range(i - 1, -1, -1):
                    if nums[j] >= i - j:
                        good_indexes[j] = True
                        index_changed = True
                        if j == 0:
                            return True
            if not index_changed:
                return False
            i = 0
            while not good_indexes[i]:
                i += 1
            index_changed = False
        return good_indexes[0]


s = Solution()
print(s.canJump([3,2,1,0,4]))