"""
1.a>0, two ends in original array are bigger than center if you learned middle school math before.

2.a<0, center is bigger than two ends.

so use two pointers i, j and do a merge-sort like process.
depending on sign of a, you may want to start from the beginning or end of the transformed array.
For a==0 case, it does not matter what b's sign is.
The function is monotonically increasing or decreasing. you can start with either beginning or end.
The idea is simple:
For a parabola,
if a >= 0, the min value is at its vertex. So our our sorting should goes from two end points towards the vertex, high to low.
if a < 0, the max value is at its vertex. So our sort goes the opposite way.
"""
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        start = 0
        end = n - 1
        i = n -1 if a >= 0 else 0
        while start <= end:
            startNum = self.getNum(nums[start],a,b,c)
            endNum = self.getNum(nums[end], a, b, c)
            if a >= 0:
                if startNum >= endNum:
                    res[i] = startNum
                    i -= 1
                    start += 1
                else:
                    res[i] = endNum
                    i -= 1
                    end -= 1
            else:
                if startNum <= endNum:
                    res[i] = startNum
                    i += 1
                    start += 1
                else:
                    res[i] = endNum
                    i += 1
                    end -= 1
        return res

    def getNum(self,x,a,b,c):
        return a * x * x + b * x + c