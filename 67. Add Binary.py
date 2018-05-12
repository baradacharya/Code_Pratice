#2. Add Two Numbers
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j>=0 or carry:
            if i >= 0: p = int(a[i])
            else: p = 0
            if j >= 0: q = int(b[j])
            else: q = 0
            curval = p + q + carry
            s += str(curval % 2)
            carry = curval/2
            i -= 1
            j -= 1
        s.reverse()
        return ''.join(s)
s = Solution()
# print s.addBinary( a = "11", b = "1")
print s.addBinary(a = "1010", b = "1011")
