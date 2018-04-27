"""
 #1 Brute Force O(mn)
 #2 Binary Search O(log(n!)) #digonal search
 #4 Search Space Reduction T: O(m + n)
"""
#Search Space Reduction
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return None

        m,n = len(matrix),len(matrix[0])
        row = m-1
        col = 0
        while col < n and row >=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        return False