# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # keeps interval ends first, as it leaves the most room for the rest.
        # take one with smallest end, remove all the bad ones overlapping it, and repeat
        intervals.sort(key=lambda l: l.end)  # sort with end
        ans = 0
        end = float('-inf')
        for interval in intervals:
            if end <= interval.start:  # can't merge
                end = interval.end
            else:  # remove can merge
                ans += 1
        return ans