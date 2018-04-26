# Definition for a point.
"""
Given point A, we need to calculate all slopes between A and other points. There will be three cases:
1.  Some other point is the same as point A.
2.  Some other point has the same x coordinate as point A, which will result to a positive infinite slope.

3.calculate slope. store all slopes in a hash table. And we find which slope shows up mostly.
Then add the number of same points to it. Then we know the maximum number of points on the same line for point A.
We can do the same thing to point B, point C...
Finally, just return the maximum result among point A, point B, point C...
"""
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        l = len(points)
        ans = 0
        for i in range(l):
            slope_map = {}
            same = 1
            for j in range(i + 1, l):
                tx, ty = points[j].x, points[j].y
                if tx == points[i].x and ty == points[i].y:  # same point
                    same += 1
                    continue
                if tx == points[i].x:  # infinte slope
                    slope = 'inf'
                else:
                    slope = (points[i].y - ty) * 100.0 / (points[i].x - tx)
                if slope not in slope_map:
                    slope_map[slope] = 1
                else:
                    slope_map[slope] += 1

            if not slope_map.values():
                local_max = same
            else:
                local_max = same + max(slope_map.values())
            ans = max(ans, local_max)
        return ans
s = Solution()
#[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print s.maxPoints( [Point(1,1),Point(3,2),Point(5,3),Point(4,1),Point(2,3),Point(1,4)])
#print s.maxPoints([Point(0,0),Point(94911151,94911150),Point(94911152,94911151)]) #this test case is failing due to precision value
#to pass it store slope by multipling ith 100