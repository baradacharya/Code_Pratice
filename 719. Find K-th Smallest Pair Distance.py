#1: Heap [Time Limit Exceeded]
#2. Time Complexity: O((k+N)logN),As k = O(N^2) O(N^2LogN)
#The complexity added by our heap operations is either O((k+N)logN) in the Java solution,
# Additionally, we add O(NlogN) complexity due to sorting.
#Space Complexity: O(N), the space used to store our heap of at most N-1 elements.
# import heapq
# class Solution(object):
#     def smallestDistancePair(self, nums, k):
#         nums.sort()
#         heap = [(nums[i+1] - nums[i], i, i+1) for i in xrange(len(nums) - 1)]
#         heapq.heapify(heap)
#         for _ in xrange(k):
#             d, i, j = heapq.heappop(heap)
#             if j + 1 < len(nums):
#                 heapq.heappush(heap,(nums[j + 1] - nums[i], i, j + 1))
#         return d

#2: Binary Search + Prefix Sum
"""
Let's binary search for the answer. It's definitely in the range [0, W], where W = max(nums) - min(nums)].Let possible(guess) be true 
if and only if there are k or more pairs with distance less than or equal to guess. We will focus on evaluating our possible function quickly.


"""
#https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/109082/Approach-the-problem-using-the-%22trial-and-error%22-algorithm
class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)
        l = 0
        r = nums[n-1]-nums[0]
        while l < r:
            count = 0
            m = l + (r-l)/2
            j = 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= m:
                    # print nums[j],nums[i],nums[j] - nums[i],m
                    j += 1
                count += j - i -1
            # print ("m ",m)
            # print("count", count)
            if count < k:
                l = m + 1
            else:
                r = m
        return l

s = Solution()
# print s.smallestDistancePair([1,3,1],1)
print s.smallestDistancePair([1,3,7,12],2)
#3: Binary Search + Sliding Window