#for each additional row, how many more rectangles are added?
#For each pair of 1s in the new row (say at new_row[i] and new_row[j]),
#we could create more rectangles where that pair forms the base.
#The number of new rectangles is the number of times some previous row had row[i] = row[j] = 1.
#A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle.
"""
count count[i, j], the number of times we saw row[i] = row[j] = 1.
 When we process a new row, for every pair new_row[i] = new_row[j] = 1,
 we add count[i, j] to the answer, then we increment count[i, j].
"""
import collections
class Solution(object):
    def countCornerRectangles(self, grid):
        count = collections.Counter()
        ans = 0
        for row in grid:
            for i in xrange(len(row)):
                if row[i]:
                    for j in xrange(i+1, len(row)):
                        if row[j]:
                            ans += count[i, j]
                            count[i, j] += 1
        return ans

s = Solution()
# print s.countCornerRectangles([[1,1,1],[1,1,1],[1,1,1]])
# print s.countCornerRectangles([[0,1,0],[1,0,1],[1,0,1],[0,1,0]])
# print s.countCornerRectangles([[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]])
print s.countCornerRectangles([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]])
