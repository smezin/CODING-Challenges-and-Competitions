class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        part = []
        parts = []
        part_counter = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != '-':
                part.append(s[i].upper())
                part_counter += 1
            if part_counter == k or i == 0:
                if part:
                    p = ''.join(part[::-1])
                    parts.append(p)
                print(p)
                part_counter = 0
                part = []
        print(parts[::-1])
        return '-'.join(parts[::-1])

s = Solution()
s.licenseKeyFormatting(s = "--a-a-a-a--", k = 2)    