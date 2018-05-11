#Like 56. Merge Intervals
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        intervals = []
        for s in schedule:
            intervals += s
        intervals.sort(key= lambda l:l.start)
        merged = [intervals[0]]
        res = []
        for interval in intervals[1:]:
            #append, calculate free time
            if interval.start > merged[-1].end:
                res.append((merged[-1].end,interval.start))
                merged.append(interval)
            else:#merge
                merged[-1].end = max(merged[-1].end,interval.end)
        return res
s = Solution()
print s.employeeFreeTime([[Interval(1,2),Interval(5,6)],[Interval(1,3)],[Interval(4,10)]])