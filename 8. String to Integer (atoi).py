class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0 : return 0
        ls = list(str.strip())
        if ls[0] == "-" : sign = -1
        else:sign = 1
        if ls[0] == '+' or ls[0] == '-': del ls[0]
        res = 0
        i = 0
        while i < len(ls) and ls[i].isdigit():
            res = res * 10 + int(ls[i])
            i +=1
        return max(-2**31, min(2**31-1,sign * res))
s = Solution()
print s.myAtoi("42")
print s.myAtoi("   -42")
print s.myAtoi("4193 with words")
print s.myAtoi("words and 987")
print s.myAtoi("-91283472332")

