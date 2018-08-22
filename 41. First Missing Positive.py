#Your algorithm should run in O(n) time and uses constant extra space.
"""
negative number exists otherwise index approach
Put each number in its right place.
When we find 5, then swap it with A[4].
At last, the first place where its number is not right, return the place + 1.
"""
class Solution(object):
    # T: O(n) S: O(1)
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #find right places for all integer(< size of array)
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < len(nums) and nums[nums[i]-1] != nums[i]: #while loop trick
                nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1]
        print nums
        for i in range(len(nums)):
            if i != nums[i] - 1:
                return i + 1
        return len(nums) + 1


    """ With O(n) extra space.
        num_set = set(nums)
        i = 1
        while 1:
            if i not in num_set:
                return i
            i += 1
    """
s = Solution()
# print s.firstMissingPositive([-1,4,2,1,9,10])
print s.firstMissingPositive([3,4,-1,1])