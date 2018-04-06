"""
11. Container With Most Water
Two pointer approach.
start from both end.
move the minnimum pointer.
T: O(n), s:O(1)
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        l  = 0
        r  = len(height)-1
        while(l<r):
            maxArea = max(maxArea, min(height[l],height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea

s = Solution()
a = s.maxArea([1,8,6,2,5,4,8,3,7])
print a