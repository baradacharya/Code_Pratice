class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 0,0 point common for row 0 and col 0 so specify col0 separately
        col0, rows, cols = 1, len(matrix), len(matrix[0])
        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for i in reversed(range(rows)):
            for j in range(cols - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
        return matrix

s = Solution()
# matrix = [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
matrix = [[1,1,1],[0,1,2]]
print s.setZeroes(matrix)