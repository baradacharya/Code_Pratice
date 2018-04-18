"""
return same number by adding one to it
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for d in digits:
            num = num * 10 + d
        return [int(i) for i in str((num+1))]

s  = Solution()
print s.plusOne([2,3,4,5])