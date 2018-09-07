"""
I am implementing this structure with a min heap.
Append interval to heap when addNum called
Merge intervals when getIntervals called
"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

from heapq import *

# class SummaryRanges(object):
#     def __init__(self):
#         self.intervals = []
#
#     def addNum(self, val):
#         heappush(self.intervals, (val, Interval(val, val)))
#
#     def getIntervals(self):
#         stack = []
#
#         while self.intervals:
#             idx, cur = heappop(self.intervals)
#             if not stack:
#                 stack.append((idx, cur))
#             else:
#                 _, prev = stack[-1]
#                 if prev.end + 1 >= cur.start:
#                     prev.end = max(prev.end, cur.end)
#                 else:
#                     stack.append((idx, cur))
#         self.intervals = stack
#         return list(map(lambda x: x[1], stack))

class SummaryRanges(object):
    def __init__(self):
        self.intervals = []

    def addNum(self, val):
        heappush(self.intervals, (Interval(val, val)))

    def getIntervals(self):
        stack = []

        while self.intervals:
            curInterval = heappop(self.intervals)
            if not stack:
                stack.append(curInterval)
            else:
                prev = stack[-1]
                if prev.end + 1 >= curInterval.start:
                    prev.end = max(prev.end, curInterval.end)
                else:
                    stack.append(curInterval)
        self.intervals = stack
        return list(stack)




        # Your SummaryRanges object will be instantiated and called as such:
        # obj = SummaryRanges()
        # obj.addNum(val)
        # param_2 = obj.getIntervals()