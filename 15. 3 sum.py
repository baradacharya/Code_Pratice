"""
 O(n^2)
 by sorting we will get a direction to move
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #3 pointer approach
        res = []
        nums.sort() #Important step
        for i in range(len(nums)-2): #first pointer
            if i>0 and nums[i] == nums[i-1]: #skip pointer with same value
                continue

            l  = i+1 #2nd pointer
            r = len(nums)-1 #3rd pointer

            while l<r:
                sum = nums[i] + nums[l] + nums[r]

                if sum == 0:
                    res.append((nums[i],nums[l],nums[r]))
                    while l < r and nums[l] == nums[l+1]: #skip pointer with same value
                        l += 1
                    while l < r and nums[r] == nums[r-1]: #skip pointer with same value
                        r -= 1
                    l +=1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return res

s = Solution()
q = s.threeSum([-1,0,1,2,-1,-4])
print q