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
        for i in range(len(digits)):
            num += digits[i] * pow(10,len(digits)-i-1)
        return [int(i) for i in str((num+1))]

s  = Solution()
num = s.plusOne([2,3,4,5])
print num