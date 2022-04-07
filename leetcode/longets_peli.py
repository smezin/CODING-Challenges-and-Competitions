class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_peli = 0
        def is_peli(word: str) ->bool:
            n = len(word)
            for i in range (n // 2):
                if word[i] != word[n - i -1]:
                    return False
            return True
        
        def get_longest(start: int) -> str:
            nonlocal longest_peli
            end = start + 1
            while is_peli(s[start:end]):
                end += 1
            end -= 1
            print(s[start:end])
            peli_len = end - start
            longest_peli = max(longest_peli, peli_len)
            return longest_peli
        
        return get_longest(1)

s = Solution()
print(s.longestPalindrome('1axaxa2'))