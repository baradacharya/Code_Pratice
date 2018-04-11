#Length approach, 2D DP (like palindrome)
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + [i for i in nums] + [1]
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for num_ballons in range(1,len(nums)-1):
            #using exclusive region notation, the lth and rth balloons are not burst in this sub - problem.
            for l in range(0,len(nums)- num_ballons-1):
                r = l + num_ballons + 1
                for m in range(l+1,r): #region (l,r), and  m is the last balloon to be burst
                    #dp[l][m] : max coins after the balloons in region (l,m) are burst
                    #dp[m][r] : max coins after the balloons in region (m,r) are burst
                    #nums[l]* nums[m]* nums[r]: coins by brusting remaing ballons,l-1,m,r+1
                    dp[l][r] = max(dp[l][r],dp[l][m] + nums[l]* nums[m]* nums[r] + dp[m][r])
        #print dp
        return dp[0][n+1]
s = Solution()
print s.maxCoins([3,1,5,8])

#1,3,1,5,8,1
#3 -> 3, 1 -> 15; 5 -> 40;  8 -> 40
#3,1 -> 3*1*5 + 1*3*5 = 30; 1,5 -> 3*1*5 + 3*5*8 = 135; 5,8 -> 1*5*8 + 1*8*1 = 48
#3,1,5 -> 3*1*5 + 3*5*8 + 3*8*1= 159; 1,5,8 -> 3*1*5 + 3*5*8 + 3*8*1 = 159
#3,1,5,8 -> 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167