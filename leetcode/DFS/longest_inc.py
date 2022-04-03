from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_row = len(matrix) - 1
        max_col = len(matrix[0]) - 1
        MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_path = 0
        
        def dfs(start, path_len = 0) -> int:
            row ,col = start
            print(f'starting at: ({row},{col})')
            for move in MOVES:
                r, c = move
                n_row = row + r
                n_col = col + c
                if n_row < 0 or n_row > max_row or n_col < 0 or n_col > max_col:
                    continue
                if matrix[n_row][n_col] <= matrix[row][col]:
                    continue
                print(f'moving to: ({n_row},{n_col})')
                return max(path_len, dfs((n_row, n_col), path_len + 1))
            return path_len
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                max_path = max(max_path, dfs((row, col)))
        return max_path

I = [[9,9,4],[6,6,8],[2,1,1]]
s = Solution()
l = s.longestIncreasingPath(I)
print(l)
