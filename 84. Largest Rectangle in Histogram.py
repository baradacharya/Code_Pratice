#https://leetcode.com/problems/largest-rectangle-in-histogram/solution/
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        ans  = 0
        for i,h in enumerate(heights):
            while stack[-1] != -1 and h <= heights[stack[-1]]: #height descends
                ans = max(ans,heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i) #height increses

        while stack[-1] != -1:
            ans = max(ans, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return ans

s = Solution()
print s.largestRectangleArea([2,1,5,6,2,3])