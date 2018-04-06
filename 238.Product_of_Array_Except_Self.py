class Solution(object):
    # def productExceptSelf(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     size = len(nums)
    #
    #     left_mul = list()
    #     right_mul = list()
    #
    #     left_mul.append(1)
    #     for i in range(size-1):
    #         left_mul.append(left_mul[-1]*nums[i])
    #
    #     right_mul.append(1)
    #     for i in range(size-1,0,-1):
    #         right_mul.append(right_mul[-1]*nums[i])
    #
    #     right_mul.reverse()
    #     for i in range(size):
    #         nums[i] = left_mul[i] * right_mul[i]
    #
    #     return nums

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list()
        p = 1
        for i in range(len(nums)):
            res.append(p)
            p *= nums[i]
        p = 1
        for i in reversed(range(len(nums))):
            res[i] *= p
            p *= nums[i]
        return res


s = Solution()
print s.productExceptSelf([1,2,3,4])