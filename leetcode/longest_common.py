class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        if rows == 0 and cols == 0:
            return 0
        
        acc_table = [[0 for _ in range(cols)] for _ in range(rows)]
        max_val = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i-1][j-1] == '1' and (i < rows and j < cols):
                    acc_table[i][j] = 1 + min(int(matrix[i][j - 1]), int(matrix[i - 1][j]))
                    max_val = max(max_val, acc_table[i][j]) 
                if i <= rows and j <= cols:
                    max_val = max(max_val, int(matrix[i-1][j]), int(matrix[i][j-1]))
        print(acc_table)
        return max_val ** 2


M = [["1","0","1","0","0"],
     ["1","0","1","1","1"],
     ["1","1","1","1","1"],
     ["1","0","0","1","0"],
     ["1","0","1","0","0"]]
M1 = [["0","1"],
      ["1","0"]]
s = Solution()
res = s.maximalSquare(M1)
print(res)