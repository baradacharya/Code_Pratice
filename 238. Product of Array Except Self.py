#Trick : Store product from left side, and right side for each i
class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         size = len(nums)
#         left_mul = list()
#         right_mul = list()
#         left_mul.append(1)
#         for i in range(size-1):
#             left_mul.append(left_mul[-1]*nums[i])
#
#         right_mul.append(1)
#         for i in range(size-1,0,-1):
#             right_mul.append(right_mul[-1]*nums[i])
#         right_mul.reverse()
#
#         for i in range(size):
#             nums[i] = left_mul[i] * right_mul[i]
#
#         return nums
    #improvement instead of storing right side multiplcation, can calculate simantanously
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list()
        res.append(1)
        for i in range(len(nums)-1):
            res.append(res[-1]*nums[i])
        p = 1
        #traverse from the right side , already calculated from the left
        for i in reversed(range(len(nums))):
            res[i] *= p
            p *= nums[i]
        return res

        """ #This code will fail if any 0 is present in the array.
        res = 1
        for num in nums:
            res *= num
        for i in range(len(nums)):
            nums[i] = res/nums[i]
        return nums
        """

s = Solution()
print s.productExceptSelf([1,2,3,4])