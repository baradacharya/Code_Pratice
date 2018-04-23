#1 Revert half of the number

# #using extra space, by using list
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0 : return False
#         l = [i for i in str(x)]
#         i,j = 0,len(l)-1
#         while i <j:
#             if l[i] != l[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True

#without extra space
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if  x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x /= 10

        return x == revertedNumber or x == revertedNumber/10 #even,odd

s = Solution()
print s.isPalindrome(1234321)
print s.isPalindrome(12345)
