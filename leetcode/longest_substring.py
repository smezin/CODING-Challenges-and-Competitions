class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        sub_size = 0
        start_index = 0
        for i in range(len(s)):
            if s[i] in letters:
                start_index = max(start_index, letters[s[i]] + 1)
            sub_size = max(sub_size, i - start_index + 1)
            letters[s[i]] = i
            
        print(letters)
        return sub_size

s = Solution()
res = s.lengthOfLongestSubstring('dvdf')
print(res)