from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        map_m = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        return self.map_matrix(matrix, map_m)
        
    def map_matrix(self, matrix, map_m):
        max_side = 0
        col, row = 0, 0
        print(map_m)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == '1':
                    up_left = 0 if row < 0 or col < 0 else map_m[row - 1][col - 1]
                    left = 0 if col < 0 else map_m[row][col - 1]
                    up = 0 if row < 0 else map_m[row - 1][col]
                    map_m[row][col] = 1 + min(up_left, left, up)
                    print(f'row:{row} col:{col} | up:{up} left:{left} upleft:{up_left} map:{map_m[row-1][col-1]}')
                    max_side = max(max_side, map_m[row][col])
        print(map_m)
        print (max_side ** 2)
        return max_side ** 2


M = [["1","0","1","0","0"],
     ["1","0","1","1","1"],
     ["1","1","1","1","1"],
     ["1","0","0","1","0"]]
s = Solution()
s.maximalSquare(M)