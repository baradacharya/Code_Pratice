#using Heap
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda l : l.start)
        heap = [] # stores the end time of intervals
        from heapq import *
        for interval in intervals:
            #compare with minnimum end time of heap
            if heap and heap[0] <= interval.start:# means two intervals can use the same room
                heapreplace(heap,interval.end) #update the end time of that room
                #heapreplace is heappop followed by heappush
            else:# a new room is allocated
                heappush(heap,interval.end)
        return len(heap)

s = Solution()
print s.minMeetingRooms([Interval(0,30),Interval(5,10),Interval(15,20)])