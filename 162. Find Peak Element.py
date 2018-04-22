#1.Linear search O(n)
#2.Binary Search O(log (n))
class Solution(object):
    # def findPeakElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     for i in len(nums):
    #         if nums[i] > nums[i+1]:
    #             return i
    #     return len(nums)-1

    #2.binary seach
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.search(nums,0,len(nums)-1)

    def search(self,nums,l,r):
        if l == r :
            return l
        m = (l + r)/2

        if nums[m] < nums[m+1]: #m is on ascending , search in right half
            return self.search(nums,m+1,r)
        else:#m is on descending , search in left half
            return self.search(nums,l,m)

    # 2.binary seach
    def findPeakElement(self, nums):
        l,r = 0 ,len(nums)
        while l < r :
            m = (l + r)/2
            if m< len(nums)-1 and nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m
        return l