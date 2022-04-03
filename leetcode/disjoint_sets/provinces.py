from typing import List
class Solution:
    
    def extract_unions(self, isConnected: List[List[int]]) -> List[List[int]]:
        unions = []
        for row in range(len(isConnected)):
            for col in range(row + 1, len(isConnected[row])):
                if isConnected[row][col] == 1:
                    unions.append([row, col])
        print(unions)
        return unions
    
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

    def find(self, v: int) -> int:
        if self.root[v] == v:
            return v
        self.root[v] = self.find(self.root[v])
        return self.root[v]
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = max(len(isConnected), len(isConnected[0]))
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        unions = self.extract_unions(isConnected)
        for union in unions:
            self.union(*union)
        roots = set()
        for i in range(len(self.root)):
            roots.add(self.find(i))
        return (len(roots))


C = [[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
    ,[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0]
    ,[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    ,[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0]
    ,[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0]
    ,[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
    ,[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0]
    ,[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
    ,[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
    ,[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]
    ,[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0]
    ,[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0]
    ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
IELS = [[1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]]
s = Solution()
print(s.findCircleNum(IELS))