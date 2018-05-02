class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start=0
        end = len(nums)-1
        while start <= end:
            mid = (start + end)/2
            if nums[mid] == target:
                l = r = mid
                while l >= 0 and nums[l] == nums[mid]:
                    l -= 1
                while r < len(nums) and nums[r] == nums[mid]:
                    r += 1
                return [l+1,r-1]
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return [-1,-1]