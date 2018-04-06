"""
Similar to the code 3sum problem. here don't take consideration of duplicates.
T: O(n^2)
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        nums.sort() #Important step
        closest =  nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            l  = i+1
            r = len(nums)-1

            while l<r:
                sum = nums[i] + nums[l] + nums[r]

                if sum == target:
                    return sum

                if(abs(target-sum)) < abs(target-closest):
                    closest = sum

                if sum < target:
                    l += 1
                else:
                    r -= 1
        return closest

s = Solution()
q = s.threeSumClosest([1,1,1,0], 100)
print q