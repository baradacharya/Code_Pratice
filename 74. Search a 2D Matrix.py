#binary search in a 2D sorted matrix
"""
m * n matrix convert to an array => matrix[x][y] => a[x * n + y]
an array convert to m * n matrix => a[x] =>matrix[x / n][x % n];
"""
# 1. Binary Search T: O(logn)
# def searchMatrix(self, matrix, target):
#     """
#     :type matrix: List[List[int]]
#     :type target: int
#     :rtype: bool
#     """
#     if not matrix: return False
#     m, n = len(matrix), len(matrix[0])
#     l, r = 0, m * n - 1
#     while l <= r:
#         mid = (l + r) / 2
#         num = matrix[mid / n][mid % n]
#         if num == target:
#             return True
#         elif num < target:
#             l = mid + 1
#         else:
#             r = mid - 1
#
#     return False

#2. Search space reduction T: O(m+n)
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix: return False
    m, n = len(matrix), len(matrix[0])
    i, j = m - 1, 0
    while i >= 0 and j < n:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            j += 1
        else:
            i -= 1
    return False

searchMatrix([[-5]], -5 )