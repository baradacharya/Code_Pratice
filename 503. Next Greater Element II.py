#Brute force TLE
# class Solution(object):
#     def nextGreaterElements(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         res = [-1] * n
#         for i in range(n):
#             for j in range(1,n):
#                 num = nums[(i+j)%n]
#                 if num > nums[i]:
#                     res[i] = num
#                     break
#         return res

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        stack = []
        for i in range(2 * n -1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i%n]:
                stack.pop()
            res[i%n] = nums[stack[-1]] if stack else -1
            stack.append(i%n)
        return res
s = Solution()
print s.nextGreaterElements([3,8,4,1,2])