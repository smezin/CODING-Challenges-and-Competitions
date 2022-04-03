from typing import List 
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        dj = Disjoint(n)
        count = n
        for time_s, a, b in logs:
            if dj.union(a, b):
                count -= 1
                print(count)
                if count == 1:
                    return time_s
    
class Disjoint:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        
    def find(self, v: int) -> int:
        if v == self.root[v]:
            return v
        self.root[v] = self.find(self.root[v])
        return self.root[v]

    def union(self, a: int, b: int) -> None:
        print(f'uniting: {a}, {b}')
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return False
       
        if self.rank[root_a] > self.rank[root_b]:
            self.root[root_b] = root_a
        elif self.rank[root_b] > self.rank[root_a]:
            self.root[root_a] = root_b
        else:
            self.root[root_a] = root_b
            self.rank[root_b] += 1
        return True

s = Solution()
I = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
s.earliestAcq(I, 6)