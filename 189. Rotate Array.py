#1. using extra space
class Solution(object):
    # def rotate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: void Do not return anything, modify nums in-place instead.
    #     """
    #     if not nums: return
    #     res =[]
    #     n = len(nums)
    #     for i in range(n-k,n):
    #         res.append(nums[i])
    #     for i in range(n-k):
    #         res.append(nums[i])
    #     for i in range(n):
    #         nums[i] = res[i]
        # n = len(nums)
        # k = k % n
        # nums[:] = nums[n - k:] + nums[:n - k]
    #2. without using extra space
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        self.reverse(nums,0 ,n-1)
        self.reverse(nums, 0,k)
        self.reverse(nums, k, n - 1)

    def reverse(self,nums,l,r):
        while l<r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -=1
s = Solution()
nums = [1,2,3,4,5,6,7]
s.rotate(nums, 3)
print nums

