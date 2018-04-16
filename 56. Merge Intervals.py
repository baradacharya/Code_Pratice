# merge([[2,6],[8,10],[1,3],[15,18]])
# merge([[1,3],[2,6],[8,10],[15,18]])
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda l:l.start)
        merged = []
        for interval in intervals:
            if not merged or interval.start > merged[-1].end:#cann't merge
                merged.append(interval)
            else: #can merge
                merged[-1].end = max(interval.end,merged[-1].end)
        return merged