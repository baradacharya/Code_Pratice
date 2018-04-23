class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        A = [[] for i in range(numRows)]
        j = 0
        down = True
        for i in range(len(s)):
            if j == numRows:
                down = False
                j = max(0,j-2)
            if j == -1:
                down = True
                j = min(numRows-1, j+2)
            if down:
                A[j].append(s[i])
                j += 1
            else:
                A[j].append(s[i])
                j -= 1
        res = ""
        for l in A:
            for c in l:
                res += c
        return res

s = Solution()
print s.convert("PAYPALISHIRING",3)
print s.convert("PAYPALISHIRING",4)
print s.convert("ABC",1)
