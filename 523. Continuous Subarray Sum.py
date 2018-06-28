#325,209,53
#Using hashmap
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        sum_count = {0: -1}
        for i in range(len(nums)):
            sum += nums[i]
            if k != 0 :
                sum = sum % k  #multiple of k
            if sum  in sum_count:
                if i - sum_count[sum] > 1:#length should greter than one
                    return True
            else:
                sum_count[sum] = i
        return False

s = Solution()
# print s.subarraySum([2, 5, 33, 6, 7, 25, 15],k=13)
print s.subarraySum([0,0],0)