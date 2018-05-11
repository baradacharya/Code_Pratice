# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        stack = []
        #Trick add new interval and merge till possible
        start = newInterval.start
        end  = newInterval.end
        i = 0
        while i < len(intervals):#Trick : while loop
            if start <= intervals[i].end: #can merge
                if end < intervals[i].start : #can't merge
                    break
                start = min(intervals[i].start,start)
                end = max(intervals[i].end,end)
            else:#cann't merge add previous intervals
                stack.append(intervals[i])
            i += 1
        stack.append(Interval(start,end))
        stack += intervals[i:]
        return stack

s = Solution()
# print s.insert([Interval(1,3),Interval(6,9)],Interval(2,5))
# print s.insert([Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)],Interval(4,8))
print s.insert([Interval(1,5)],Interval(2,3))