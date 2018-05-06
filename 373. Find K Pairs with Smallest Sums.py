#1. Build a minHeap of elements from the first array.
#2. Do the following operations k-1 times :
#pop out the Top Element in Heap,
#replace the top with the next element from the diff array.
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m,n = len(nums1),len(nums2)
        if m == 0 or n == 0: return []
        import heapq
        heap = []
        res = []
        for i in range(m):
            heapq.heappush(heap, (nums1[i] + nums2[0],i, 0))
        for count in range(min(k,m*n)):
            sum,i,j = heapq.heappop(heap)
            res.append((nums1[i],nums2[j]))
            if j == n - 1:
                continue
            heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
        return res
s = Solution()
print s.kSmallestPairs([1,2,4],[-1,1,2],100)
