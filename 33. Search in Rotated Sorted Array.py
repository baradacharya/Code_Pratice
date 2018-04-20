class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        l,h = 0,len(nums)-1
        while l <=h :
            m = (l + h)/2
            if target == nums[m]: return m
            #Trick : always look the target in the sorted side if not found look in the other side.
            # First decide the sorted side
            if nums[l] <= nums[m]: # left side is sorted
                if nums[l] <= target <= nums[m]: #if target lies between l and m
                    h = m - 1
                else: #look in the other side
                    l = m + 1
            else: #nums[l] > nums[m] #right side is sorted
                if nums[m] <= target <= nums[h]:
                    l = m + 1 #if target lies between m and r
                else: #look in the other side
                    h = m - 1
        return -1

s  = Solution()
print s.search([4,5,0,1,2,3,4],0)
