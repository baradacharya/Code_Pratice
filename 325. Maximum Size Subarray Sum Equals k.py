#one pointewr, hash map for storing sum  and index (sum from starting upto that index)
#209. Minimum Size Subarray Sum
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        cur_sum  =  0
        sum_map = {0:-1}#sum_value:index (sum up to index)
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum == k: #update new max length
                ans = i+1
            elif cur_sum-k in  sum_map:
                ans = max(ans,i-sum_map[cur_sum-k])
            if cur_sum not in sum_map:#add this sum to map
                sum_map[cur_sum] = i
        return ans

s = Solution()
# print s.maxSubArrayLen([1, -1, 5, -2, 3],3)
print s.maxSubArrayLen([-2,-1,2,1],1)

