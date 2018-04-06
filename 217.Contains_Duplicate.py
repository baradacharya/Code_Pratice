class Solution(object):
    #T:O(n), S:O(n)
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False

    # #T:O(nlogn) S:O(1)
    # def containsDuplicate(self, nums):
    #     nums.sort()
    #     for i in range(len(nums)):
    #         if nums[i] == nums[i+1]:
    #             return True
    #         else:
    #             return False

