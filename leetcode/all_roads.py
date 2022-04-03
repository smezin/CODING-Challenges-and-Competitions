from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n != len(edges) - 1:
            return False
        uf = UnionFind(n)
        for edge in edges:
            uf.union()
        print(uf.root)
        
        
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        
    def find(self, v: int) -> int:
        if self.root[v] == v:
            return v
        self.root[v] = self.find(self.root[v])
        return self.root[v]
    
    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.root[root_b] = root_a
            elif self.rank[root_b] > self.rank[root_a]:
                self.root[root_a] = root_b
            else:
                self.root[root_a] = root_b
                self.rank[root_b] += 1