#1 Simple Sorting [Time Limit Exceeded]
#17 / 18 test cases passed. (TLE)
# class MedianFinder(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.data = []
#         self.size  = 0
#
#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: void
#         """
#         self.data.append(num)
#         self.size += 1
#
#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         self.data.sort()
#         if self.size & 1:
#             return self.data[self.size / 2]
#         else:
#             return (self.data[self.size / 2 - 1] + self.data[self.size / 2]) * 0.5

###2. Two Heaps
"""
we only need a consistent way to access the median elements.
Keeping the entire input sorted is not a requirement.
A max-heap to store the smaller half of the input numbers
A min-heap to store the larger half of the input numbers
T: O(log n) insert O(log n) median O(1), space : O(n)
"""
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = [] #max heap, lower half array
        self.hi = [] #min heap, larger half array
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        from heapq import *
        # python has by default ue min heap, so for max heap has to store negative num
        # min heap(hi) size always greter than max heap(lo)
        #before pushing into a heap ,push and pop into the other heap
        if len(self.lo) == len(self.hi): #will add to hi
            heappush(self.hi,-heappushpop(self.lo,-num))
        else:
            heappush(self.lo,-heappushpop(self.hi,num))
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.hi) == len(self.lo):
            return (self.hi[0] - self.lo[0])*0.5
        else:
            return self.hi[0]


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print obj.findMedian()
obj.addNum(3)
print obj.findMedian()