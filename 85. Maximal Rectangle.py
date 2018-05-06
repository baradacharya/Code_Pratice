"""
left,right stores information about previous row.

left : max point where rectangle starts, right: min point where rectangle finishes.

height : height of current rectangle.

left(i,j) = max(left(i-1,j), cur_left) ; cur_left can be determined from the current row

right(i,j) = min(right(i-1,j), cur_right); cur_right can be determined from the current row

height(i,j) = height(i-1,j) + 1, if matrix[i][j]=='1';

height(i,j) = 0, if matrix[i][j]=='0'

Area =  [right(i,j) - left(i,j)]*height(i,j).
"""
#Dynamic Programming approach
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m,n = len(matrix),len(matrix[0])
        left = [0] * n
        right = [n] * n
        height = [0] * n
        maxArea = 0
        for i in range(m):
            cur_left,cur_right =0,n
            #calculation of left array
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j],cur_left)
                else:
                    left[j] = 0
                    cur_left = j+1

            #calculation of right array
            for j in reversed(range(n)):
                if matrix[i][j] == '1':
                    right[j] = min(right[j],cur_right)
                else:
                    right[j] = n
                    cur_right = j

            #calculation of height array
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            #calculate area of rectangle
            print left, right, height
            for j in range(n):
                maxArea = max(maxArea,(right[j]-left[j])*height[j])

        return maxArea

s = Solution()
# print s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print s.maximalRectangle([["1"]])

