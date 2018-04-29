class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num  = '1'
        while n >1:
            n -= 1
            res = ""
            count = 1
            c = num[0]
            for i in range(1,len(num)):
                if num[i] == c: #count for same  ch
                    count += 1
                else:#diif ch add prev ch with count
                    res += str(count)
                    res += c
                    c = num[i]
                    count = 1
            res += str(count)
            res += c
            num = res
        return num

s = Solution()
print s.countAndSay(5)