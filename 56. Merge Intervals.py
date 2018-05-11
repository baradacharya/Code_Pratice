
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
s = Solution()
print s.merge([Interval(2,6),Interval(8,10),Interval(1,3),Interval(15,18)])
print s.merge([[1,3],[2,6],[8,10],[15,18]])