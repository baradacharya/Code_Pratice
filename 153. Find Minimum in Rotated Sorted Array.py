#Binary Search
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] <= nums[j]: #means array is sorted so 1st element will be smallest
                return nums[i]
            #will find the lowest in rotated half
            m = (i+j)/2
            if nums[i] <= nums[m]: #left side is sorted,right is rotated
                i = m + 1 #search in right half
            else:#right side is sorted,left is rotated
                j = m #search in left half

s = Solution()
print s.findMin([3,1,2])