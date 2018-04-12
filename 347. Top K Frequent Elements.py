class Solution(object):
    # #using builtin counter and most common variable.
    # def topKFrequent(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     import collections
    #     count  = collections.Counter(nums)
    #     t = zip(*count.most_common(k))[0]
    #     return t

    #using minnimum heap
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        freq_list = []
        for num in nums:
            if num in freq: freq[num] += 1
            else: freq[num] = 1
        for key in freq:
            freq_list.append((-freq[key],key))
        import heapq
        heapq.heapify(freq_list) #-ve count ,because we r using min heap
        topk = []
        for i in range(0, k):
            topk.append(heapq.heappop(freq_list)[1])
        return topk


s = Solution()
print s.topKFrequent([1,1,1,2,2,3],2)