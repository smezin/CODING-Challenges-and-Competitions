from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        CONNECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        islands = 0
    
        def dfs(row, col):
            grid[row][col] = '0'
            for r in grid:
                print(r)
            for r, c in CONNECTIONS:
                n_row = row + r
                n_col = col + c
                if n_row < 0 or n_row > max_row or n_col < 0 or n_col > max_col:
                    continue
                if grid[n_row][n_col] == '0':
                    continue
                return dfs(n_row, n_col)
                
        while self.get_first_land(grid):
            start_row, start_col = self.get_first_land(grid)
            dfs(start_row, start_col)
            islands += 1
        print(islands)
    
    def get_first_land(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    return (row, col)
        return 

s = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
s.numIslands(grid)