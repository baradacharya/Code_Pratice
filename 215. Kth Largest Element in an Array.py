#O(N lg N) running time + O(1) memory
#https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60294/Solution-explained
class Solution(object):
    #T:O(logn) S:O(k)
    def findKthLargest(self, nums, k):#best time
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        from heapq import *
        heap = []
        for i in range(len(nums)):
            heappush(heap,nums[i])
            if len(heap) > k:
                heappop(heap)
        return heap[0]

    # #T:O(logk) S:O(logk)
    # def findKthLargest(self, nums, k):  # better time, best space
    #         """
    #         :type nums: List[int]
    #         :type k: int
    #         :rtype: int
    #         """
    #         if not nums: return 0
    #         import heapq
    #         priorty_queue = []
    #         heapq.heapify(priorty_queue)
    #         for num in nums:
    #             heapq.heappush(priorty_queue,num)
    #             if len(priorty_queue) > k:
    #                 heapq.heappop(priorty_queue)
    #         return priorty_queue[0]


    # def findKthLargest(self, nums, k):#more time
    #     if not nums: return 0
    #     import heapq
    #     heapq.heapify(nums)
    #     for i in range(len(nums)-k+1):
    #         t = heapq.heappop(nums)
    #     return t


# O(n) time, quick sort
class Solution:
    # @param {integer[]} nums
    def findKthLargest(self, nums, k):
        pivot = nums[len(nums)//2]
        left  = [l for l in nums if l < pivot]
        equal = [e for e in nums if e == pivot]
        right = [r for r in nums if r > pivot]#larger half
        if k <= len(right):#if k in larger half
            return self.findKthLargest(right, k)
        elif (k - len(right)) <= len(equal):#if k  in equal
            return equal[0]#any number from equal
        else:
            return self.findKthLargest(left, k - len(right) - len(equal))