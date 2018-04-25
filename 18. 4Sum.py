#implement a  2-pointer to solve 2-sum,
#  recursion to reduce the N-sum to 2-sum.
# Some optimization was be made knowing the list is sorted.
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(nums, target, N, result, results):
            #early termination
            if len(nums)< 2 or N < 2:
                return
            if N==2:
                l,r = 0,len(nums)-1
                while l < r:
                    sum = nums[l] + nums[r]
                    if sum == target:
                        results.append(result + [nums[l],nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
                    elif sum < target:
                        l += 1
                    else:
                        r -= 1
            else:# recursively reduce N
                for i in range(len(nums)- N + 1):
                    if i==0 or i > 0 and nums[i] != nums[i-1]:
                        findNsum(nums[i+1:],target-nums[i],N-1,result+[nums[i]],results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results

s  = Solution()
print s.fourSum(nums = [1, 0, -1, 0, -2, 2],  target = 0)