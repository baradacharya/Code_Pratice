class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return False
        l,r = 0 ,len(nums)-1
        while l <= r:
            m = (l + r)/2
            if nums[m] == target: return True
            #The only difference from the first one, trickly case, just updat left and right
            if nums[l] == nums[m] and nums[r] == nums[m]:#[3 1 2 3 3 3 3]
                l += 1
                r -= 1
            elif nums[l] <= nums[m]:# left side is sorted
                if nums[l] <= target < nums[m]:#if target lies between l and m
                    r = m-1
                else:#look in the other side
                    l = m+1
            else:#right side is sorted
                if nums[m] < target <= nums[r]:#if target lies between m and r
                    l = m + 1
                else:#look in the other side
                    r = m - 1
        return False