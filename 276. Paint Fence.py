"""
https://leetcode.com/problems/paint-fence/discuss/71150/Python-solution-with-explanation
You either paint the same color with the previous one, or differently.
Since there is a rule: "no more than two adjacent fence posts have the same color."
from 2.1, since previous two are in the same color, next one you could only paint differently,
and it would form one part of "paint differently" case in the n == 3 level,
and the number of ways to paint this way would equal to same*(k-1).
from 2.2, since previous two are not the same, you can either paint the same color this time (dif*1) ways to do so,
or stick to paint differently (dif*(k-1)) times.

"""
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same, dif = k, k * (k - 1)
        for i in range(3, n + 1):
            temp = dif * 1
            dif = same * (k - 1) + dif * (k - 1)
            same = temp
        return same + dif
s = Solution()
print s.numWays(3,3)