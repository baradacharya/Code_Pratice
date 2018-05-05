"""
left,right stores information about previous row.
left : max point where rectangle start, right: min point where rectangle finish.
left(i,j) = max(left(i-1,j), cur_left) ; cur_left can be determined from the current row

right(i,j) = min(right(i-1,j), cur_right); cur_right can be determined from the current row

height(i,j) = height(i-1,j) + 1, if matrix[i][j]=='1';

height(i,j) = 0, if matrix[i][j]=='0'

Area =  [right(i,j) - left(i,j)]*height(i,j).
"""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m,n = len(matrix),len(matrix[0])
