#1. Build a minHeap of elements from the first row.
#2. Do the following operations k-1 times :
#pop out the Top Element in Heap,
#replace that root with the next element from the same column.
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        if not matrix : return 0
        m,n = len(matrix), len(matrix[0])
        heap = []
        for j in range(n):
            heapq.heappush(heap,(matrix[0][j],0,j))
        for count in range(k-1):
            val, i,j = heapq.heappop(heap)
            if i == m-1: continue #last row
            heapq.heappush(heap,(matrix[i+1][j],i+1,j))
        return heapq.heappop(heap)[0]

s = Solution()
print s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8)





