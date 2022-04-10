from collections import defaultdict
from typing import List
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        sqrs = []
        results = []
        prefix_map = defaultdict(list)
        
        
        def get_starts_with(prefix: str) -> List[str]:
            word_list = []
            for w in words:
                if w.startswith(prefix):
                    word_list.append(w)
            return word_list
        
        for w in words:
            for i in range(1, n):
                prefix_map[w[:i]] = get_starts_with(w[:i])
        print(prefix_map)
        
        def rec(step: int, sqrs: List[str]):
            if len(sqrs) == n:
                results.append(sqrs[:])
                return
            prefix = ''.join([word[step] for word in sqrs])
            print(f'{prefix} -> {prefix_map[prefix]}')
            for option in prefix_map[prefix]:
                sqrs.append(option)
                rec(step + 1, sqrs)
                sqrs.pop()
        
        for w in words:
            sqrs = [w]
            rec(1, sqrs)
        return results
        
        
W1 = ["area","lead","wall","lady","ball"]
s = Solution()
res = s.wordSquares(W1)
print(res)