class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) != 1:
            sum = 0
            for d in str(num):
                sum += int(d)
            num = sum
        return num