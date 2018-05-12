# Using 2 pointers
class Solution(object):
    def maxSubArrayLen(self,s, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        l = 0
        maxnum = 2**31-1
        min_len = maxnum
        cur_sum = 0
        for r,num in enumerate(nums):
            cur_sum += num
            while cur_sum >= s:
                min_len = min(min_len,r-l+1)
                cur_sum -= nums[l]
                l += 1
        return min_len if min_len!= maxnum else 0
s = Solution()
print s.maxSubArrayLen(7,[2,3,1,2,4,3])
