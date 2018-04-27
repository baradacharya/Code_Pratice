"""
Keep indexes of good candidates in deque deque.
the first deque element is the index of the largest window value[leftmost]
indexes in d are from the current window, they're increasing, and their corresponding nums are decreasing
For each index i:
1. Pop (from the right) indexes of smaller elements (they'll be useless).
2. Append the current index.
3. Pop (from the left) the index i - k, if it's still in the deque (it falls out of the window).
4. If our window has reached size k, append the current window maximum to the output.

"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        dq = collections.deque()
        res = []
        for i,num in enumerate(nums):
            while dq and nums[dq[-1]] < num: #1. remove numbers less than current num from right(not needed)
                dq.pop()
            dq.append(i)#2. append current index
            if dq[0] == i-k: #3. leftmost index fall out of window, remove it
                dq.popleft()
            if i >= k-1: #i reached window size
                res.append(nums[dq[0]])#add leftmost num(larget) to result
        return res

s = Solution()
print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)



