class Solution(object):
    # def majorityElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     from collections import Counter
    #     c = Counter(nums)
    #     return c.most_common(1)[0][0]

    def majorityElement(self, nums):#Faster
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) / 2]

s = Solution()
print s.majorityElement([1,2,2,2,3,4])


        