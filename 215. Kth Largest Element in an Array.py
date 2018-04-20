class Solution(object):
    #T:O(logn) S:O(n)
    def findKthLargest(self, nums, k):#best time
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        import heapq
        for i in range(len(nums)):
            nums[i] = -1 * nums[i] #because this is a minheap
        heapq.heapify(nums)
        for i in range(k):
            t = heapq.heappop(nums)
        return -1 * t

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

s = Solution()
print s.findKthLargest([3,2,1,5,6,4],k = 2)