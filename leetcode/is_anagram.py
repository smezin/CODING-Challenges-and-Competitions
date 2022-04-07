from collections import defaultdict


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    sl = list(s)
    tl = list(t).sort()
    print(sl, tl)
    return sl == tl

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters_dict = defaultdict(int)
        for i in range(len(s)):
            letters_dict[s[i]] += 1
            letters_dict[t[i]] -= 1
        return all(v == 0 for v in letters_dict.values())

is_anagram1('car', 'rat')