from typing import List
from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs:
            return s
        n = len(s)
        uf = UnionFind(n)
        for pair in pairs:
            uf.union(*pair)
        letters = defaultdict(list)
        for i in range(n):
            uf.find(i)
            letters[uf.root[i]].append(s[i])
        for key in letters:
            letters[key].sort(reverse=True)
        print(letters, uf.root)
        smallest = []
        for i in range(n):
            group = letters[uf.root[i]]
            letter = group.pop()
            smallest.append(letter)
        return ''.join(smallest)

        
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        
    def find(self, v: int) -> int:
        if self.root[v] == v:
            return v
        self.root[v] = self.find(self.root[v])
        return self.root[v]
    
    def union(self, a, b) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.root[root_b] = root_a
                print(f'putting a{root_a} in index b{root_b} ')
            elif self.rank[root_b] > self.rank[root_a]:
                self.root[root_a] = root_b
                print(f'putting b{root_b} in index a{root_a} ')
            else:
                self.root[root_b] = root_a
                print(f'putting a{root_a} in index b{root_b} ')
                self.rank[root_a] += 1
            print(a,b, self.root)
            return True
        return False
                
s = Solution()
res = s.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]])
print(res)