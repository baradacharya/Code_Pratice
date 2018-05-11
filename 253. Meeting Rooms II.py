#using Heap
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        import heapq
        intervals.sort(key = lambda l :l.start)
        heap = [] # stores the end time of intervals
        for interval in intervals:
            if heap and heap[0] <= interval.start: # means two intervals can use the same room
                heapq.heapreplace(heap,interval.end) #update the end time of that room
            else:# a new room is allocated
                heapq.heappush(heap,interval.end)
        return len(heap)