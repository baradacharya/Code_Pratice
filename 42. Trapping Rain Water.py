"""
For a given index i:
1. Find Maximum height of bar from leftside upto index i -> max_left
2. Find Maximum height of bar from rightside upto index i -> max_right
3. Add min(max_left[i],max_right[i])-height[i] to ans
T:O(n) S:O(n)
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == None:
            return 0

        size = len(height)
        max_left = [0] * size
        max_right = [0] * size
        ans = 0

        max_left[0] = height[0]
        for i in range(1,size):
            max_left[i] = max(height[i],max_left[i-1])

        max_right[size-1] = height[size-1]
        for i in range(size-2,-1,-1):
            max_right[i] = max(height[i],max_right[i+1])

        for i in range(size):
            ans += min(max_left[i],max_right[i])-height[i]
        return ans


s = Solution()
q = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print q