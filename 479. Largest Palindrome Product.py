class Solution(object): # Memory Limit Exceeded
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 9
        upper = pow(10,n) -1
        lower = pow(10,n-1)
        for i in range(upper,lower-1,-1):
            cand = self.buildPalindrome(i)
            j = upper
            while j * j >= cand:
                if cand %j == 0 and cand/j <= upper:
                    return cand % 1337
                j -= 1
        return -1
    def  buildPalindrome(self,num):
        s = list(str(num))
        s.reverse()
        return int(str(num)+ ''.join(s))

# class Solution(object): # Memory Limit Exceeded
#     def largestPalindrome(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 1: return 9
#         mod = pow(10,n)
#         upper = pow(10,n) -1
#         prod = upper * upper
#         right = prod % mod
#         left = prod / mod
#         if left == self.reverse(right): return prod % mod
#         if left > right: left -= 1
#         prod = left * mod + self.reverse(right)
#         while left != mod/10:
#             j = upper
#             while j * j >= prod:
#                 if prod %j == 0:
#                     return prod % 1337
#                 j -= 1
#             left -= 1
#             prod = left * mod + self.reverse(right)
#         return prod%1337
#
#     def  reverse(self,num):
#         s = list(str(num))
#         s.reverse()
#         return int(''.join(s))

s = Solution()
print s.largestPalindrome(2)