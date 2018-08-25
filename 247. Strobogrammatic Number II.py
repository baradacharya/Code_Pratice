class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n,n)

    def helper(self,n,m):
        if n == 0 :
            return [""]
        if n ==1 :
            return ["0","1","8"]
        list = self.helper(n-2,m)
        print ("list:",list)
        res = []
        for s in list:
            if n != m:
                res.append("0"+s+"0")
            res.append("1" + s + "1")
            res.append("6" + s + "9")
            res.append("8" + s + "8")
            res.append("9" + s + "6")
        return res

s = Solution()
# print s.findStrobogrammatic(2)
# print s.findStrobogrammatic(3)
print s.findStrobogrammatic(6)