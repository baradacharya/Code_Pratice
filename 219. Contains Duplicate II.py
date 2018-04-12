class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] in num_dict:
                if i - num_dict[nums[i]] <= k:
                    return True
            num_dict[nums[i]] = i #update with latest index
        return False

s = Solution()
print s.containsNearbyDuplicate([-1,-1],1)