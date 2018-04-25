class Solution(object):
    # T: O(n) S: O(1)
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #find right places for all integer(< size of array)
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:#trick while loop,swap untill not in right place
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(len(nums)):
            if i != nums[i] - 1:
                return i + 1
        return len(nums) + 1
s = Solution()
print s.firstMissingPositive([-1,4,2,1,9,10])