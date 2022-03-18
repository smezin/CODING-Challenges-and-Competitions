class Solution(object):
  
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        start = 0
        change = 1
        end = 0
        max_subset = 0

        if len(fruits) == 1:
            return 1
        while start < len(fruits):
            while change < len(fruits) and fruits[start] == fruits[change]:
                change += 1
            end = change + 1
            while end < len(fruits) and (fruits[change] == fruits[end] or fruits[start] == fruits[end]):
                end += 1
            if len(fruits[start:end]) > max_subset:
                max_subset = len(fruits[start:end])
                if max_subset >= len(fruits) - start:
                    break
            start = change
            change = start + 1
        return max_subset

s = Solution()
