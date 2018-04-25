
class Solution(object):
    #clockwise rotate: first reverse up to down, then swap the symmetry
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        return matrix

    #anti-clockwise rotate:  first reverse left to right line wise, then swap the symmetry
    def antirotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            matrix[i].reverse()
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


s = Solution()
print s.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])
print s.antirotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])
