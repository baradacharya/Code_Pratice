#325,209,53
#Using hashmap
#cumlative sum,num_time
#https://leetcode.com/problems/subarray-sum-equals-k/solution/
"""
if the cumulative sum upto two indices, say ii and jj is at a difference of kk i.e. if sum[i] - sum[j] = k
the sum of elements lying between indices ii and jj is kk.
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sum = 0
        sum_count = {0:1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in sum_count:
                count += sum_count[sum - k]
            sum_count[sum] = sum_count.get(sum,0) + 1
        return count
s = Solution()
print s.subarraySum([3,4,7,2,-3,1,4,2,1],7)