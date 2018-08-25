class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        i = 0
        j = len(num) -1
        while i <= j:
            if num[i]+num[j] not in "00 11 88 696":
                return False
            i += 1
            j -= 1
        return True
