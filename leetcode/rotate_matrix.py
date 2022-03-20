from re import L


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        self.reverse_rows(matrix)
        self.transpose(matrix)
        self.print_m(matrix)

    def reverse_rows(self, matrix):
        for i in range(len(matrix)//2):
            matrix[i], matrix[len(matrix)-1-i] = matrix[len(matrix)-1-i], matrix[i]

    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j] = matrix[i][j] ^ matrix[j][i]
                matrix[j][i] = matrix[i][j] ^ matrix[j][i]
                matrix[i][j] = matrix[i][j] ^ matrix[j][i]
               
    def print_m(self, matrix):
        for r in matrix:
            print(r)

M = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]

M1 = [[1,2,3],
    [4,5,6],
    [7,8,9]]

s = Solution()
s.rotate(M)

