# class Solution(object):
#     def multiply(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         return str(int(num1)*int(num2))


#`num1[i] * num2[j]` will be placed at indices `[i + j`, `i + j + 1]`
#Without using any built-in BigInteger library or convert the inputs to integer directly.
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m,n = len(num1),len(num2)
        ans = ['0'] * (m+n)
        for i in range(m-1,-1,-1):
            carry = 0
            for j in range(n-1,-1,-1):
                temp = int(ans[i+j+1]) + int(num1[i]) * int(num2[j]) + carry
                ans[i+j+1] = str(temp % 10)
                carry = temp /10

            ans[i+0] = str(int(ans[i]) + carry)
        res = ''.join(ans)
        res = res.lstrip('0')
        return res

s = Solution()
# print s.multiply("2","3")
print s.multiply( num1 = "123", num2 = "456")

