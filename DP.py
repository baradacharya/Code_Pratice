#746. Min Cost Climbing Stairs
# def minCostClimbingStairs(cost):
#     """
#     :type cost: List[int]
#     :rtype: int
#     """
#     c = []
#     c.append(0)
#     c.append(0)
#     for i in range(2, len(cost)+1):
#         temp = min(c[i - 1] + cost[i - 1], c[i - 2] + cost[i - 2])
#         c.append(temp)
#     return c[i]
# c = minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
# print(c)


# #376. Wiggle Subsequence
# import numpy as np
# def wiggleMaxLength(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if len(nums)< 2:
#         return len(nums)
#     up =  [0] * len(nums)
#     down= [0] * len(nums)
#
#     for i in range(1,len(nums)):
#         for j in range(i):
#             if nums[i] > nums[j]:
#                 up[i] = max(up[i],1 + down[j])
#             elif nums[i] < nums[j]:
#                 down[i] =  max(1 + up[j],down[i])
#     return 1 + max(up[len(nums)-1],down[len(nums)-1])
# a = wiggleMaxLength([1,7,4,9,2,5])
# print(a)

# #322. Coin Change
# def coinChange(coins, amount):
#     """
#     :type coins: List[int]
#     :type amount: int
#     :rtype: int
#     """
#     A = [amount + 1 for i in range(amount + 1)] #amount+1 for checking -1 condition
#     A[0] = 0
#     for i in range(1, amount + 1):
#         for j in range(len(coins)):
#             if (coins[j] <= i):
#                 A[i] = min(A[i], A[i - coins[j]] + 1)
#     if A[amount] > amount:
#         return -1
#     else:
#         return A[amount]
#
# t = coinChange([474,83,404,3],264)
# print(t)

# #300. Longest Increasing Subsequence
# def lengthOfLIS(self, nums):
#     if(len(nums) == 0):
#         return 0
#     A = [1] * len(nums)
#     max_ = 1
#     for i in range(len(nums)):
#         for j in range(i):
#             if (nums[j] < nums[i]):
#                 A[i] = max(A[j]+1,A[i])
#                 max_ = max(max_,A[i])
#     return max_
# d = lengthOfLIS([2,2])
# print(d)

# # 70. Climbing Stairs
# def climbStairs(n):
#     """
#     :type cost: List[int]
#     :rtype: int
#     """
#     if n==0:
#         return 0
#     c = []
#     c.append(1)
#     c.append(2)
#     for i in range(2,n):
#         temp = c[i - 1] + c[i - 2]
#         c.append(temp)
#     return c[n-1]
# c = climbStairs(4)
# print(c)

# #64. Minimum Path Sum
# def minPathSum( grid):
#     """
#     :type grid: List[List[int]]
#     :rtype: int
#     """
#     m = len(grid)
#     n = len(grid[0])
#
#     for i in range(1,m):
#         grid[i][0] += grid[i-1][0]
#     for i in range(1,n):
#         grid[0][i] += grid[0][i-1]
#     for i in range (1,m):
#         for j in range(1,n):
#             grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
#     return grid[-1][-1]
# minPathSum([[1,3,1],[1,5,1],[4,2,1]])

# #139. Word Break
# def wordBreak(s, wordDict):
#     ok = [True]
#     for i in range(1,len(s)+1):
#         ok.append(any(ok[j] and s[j:i] in wordDict for j in range(i)))
#     return ok[-1]
# print wordBreak("leetcode",["leet", "code"])

# # #140. Word Break II
# #Idea is to get the prefix word then break the string and pass the rest of the string to a recursive function.
# #store word in m/m to avoid recalculation(optional)(memory)(without it TLE will occured)(imp concept)
# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         return self.helper(s, wordDict, {})
#
#     def helper(self, s, wordDict, memo):
#         if s in memo: return memo[s] # if we calculated earlier return result to save time
#         if not s:
#             return []
#         res = []
#         for word in wordDict:#Test for each word
#             if not s.startswith(word):#for finding prefix
#                 continue
#             if len(s) == len(word):
#                 res.append(word)
#             else:
#                 #Calculate for rest of the string
#                 restofTheString = self.helper(s[len(word):],wordDict,memo) #will return all possible strings
#                 for w in restofTheString:
#                     w = word + " " + w
#                     res.append(w)
#         memo[s] = res #add string to memory to avoid recalculation (list of dict)
#         return res
#
# s = Solution()
# t = s.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])
# print(t)

#96. Unique Binary Search Trees I
#https://www.quora.com/Given-n-how-many-structurally-unique-BSTs-binary-search-trees-that-store-values-1-to-n-are-there-How-would-I-come-up-with-the-solution-Can-you-explain-the-thought-process-that-leads-to-the-solution
# def generateTrees(n):
#     """
#     :type n: int
#     :rtype: List[TreeNode]
#     """
#     #c = c(0)c(n-1)+c(1)(n-2) + ..
#     c =[0] * (n+1)
#     c[0] = 1
#     c[1] = 1
#     for i in range(2,n+1):
#         for j in range(1,i+1):
#             c[i] += c[j-1]*c[i-j]
#     return c[-1]
# t = generateTrees(3)
# print(t)

# #95. Unique Binary Search Trees II
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution(object):
#     def generateTrees(self, n):
#         """
#         :type n: int
#         :rtype: List[TreeNode]
#         """
#         if n == 0:
#             return []
#         return self.dfs(1, n + 1)
#
#     def dfs(self, start, end):
#         if start == end:
#             return None
#         result = []
#         for i in xrange(start, end):
#             for l in self.dfs(start, i) or [None]:
#                 for r in self.dfs(i + 1, end) or [None]:
#                     node = TreeNode(i)
#                     node.left, node.right = l, r
#                     result.append(node)
#         return result
# s = Solution()
# t = s.generateTrees(3)
# print t



# # 62. Unique Paths
# def uniquePaths(m, n):
#     """
#     :type m: int
#     :type n: int
#     :rtype: int
#     """
#     A = [[1 for i in range(n)] for j in range(m)]
#     for i in range(1,m):
#         for j in range(1,n):
#             A[i][j] = A[i-1][j] + A[i][j-1]
#
#     return A[-1][-1]
# print uniquePaths(3,7)

#63. Unique Paths II
# def uniquePathsWithObstacles(obstacleGrid):
#     """
#     :type obstacleGrid: List[List[int]]
#     :rtype: int
#     """
#     m = len(obstacleGrid)
#     n = len(obstacleGrid[0])
#     obstacleGrid[0][0] = 1 - obstacleGrid[0][0] #revert 1st position
#
#     for i in range(1,n):
#         if not obstacleGrid[0][i]: #0
#             obstacleGrid[0][i]  =  obstacleGrid[0][i-1]
#         else:
#             obstacleGrid[0][i] =  0
#
#     for i in range(1,m):
#         if not obstacleGrid[i][0]:
#             obstacleGrid[i][0] = obstacleGrid[i-1][0]
#         else:
#             obstacleGrid[i][0] =  0
#
#     for i in range(1,m):
#         for j in range(1,n):
#             if not obstacleGrid[i][j]:
#                 obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
#             else:
#                 obstacleGrid[i][j] = 0
#     return obstacleGrid[-1][-1]
# print uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])

# #714. Best Time to Buy and Sell Stock with Transaction Fee
# def maxProfit(prices, fee):
#     """
#     Transaction fee for one cycle buy and sell. so we will deduct fee while selling
#     cash : the maximum profit if we did not have a share of stock
#     possible in two ways 1. we didn't have share previously (cash)
#                          2. we have(hold) but we sell on a given day(hold + prices[i] - fee)
#     hold :  the maximum profit we could have if we owned a share of stock.
#     possible in two ways 1. we have share previously (hold)
#                          2. we did n't have (cash) but we buy on a given day(cash  - prices[i])
#     start with cash = 0 #didn't have share, hold = -prices[0] #buy 1st salary
#     :param prices:
#     :param fee:
#     :return:
#     """
#     cash, hold  = 0, -prices[0]
#     for  i in range(1,len(prices)):
#         cash = max(cash,    hold + prices[i]- fee)
#         hold = max(hold,    cash - prices[i])
#     return cash
# maxProfit([1, 3, 2, 8, 4, 9],2)

# #121. Best Time to Buy and Sell Stock
# def maxProfit(prices):
#     """
#     largest peak following the smallest valley.
#     minprice  : the smallest valley
#     maxprofit :maximum difference between selling price and minprice obtained so far respectively.
#     """
#     if (len(prices) == 0 or len(prices) == 1):
#         return 0
#     max_profit = 0
#     min_ = prices[0]
#     for i in range(1,len(prices)):
#         min_ = min(prices[i], min_)
#         max_profit = max(max_profit,prices[i]- min_)
#
#     return max_profit
# t = maxProfit([7, 1, 5, 3, 6, 4])
# print(t)
# #53. Maximum Subarray
# def maxSubArray(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if not nums:
#         return 0
#     maxSum = curSum = nums[0]
#     for num in nums[1:]:
#         curSum = max(num,curSum + num)
#         maxSum = max(maxSum, curSum)
#     return maxSum
# print maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

#152. Maximum Product Subarray
# def maxProduct(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if not nums:
#         return 0
#     maximum = big = small = nums[0]
#     bigtemp = smalltemp = nums[0]
#     for num in nums[1:]:
#         bigtemp = max(num, big * num, small * num)
#         smalltemp = min(num, big * num, small * num)
#         maximum = max(bigtemp, maximum)
#         big = bigtemp
#         small = smalltemp
#     return maximum
# print maxProduct([2,3,-2,4])
# print  maxProduct([-2,-1,-3,-4])
# print maxProduct([2,3,-2,4,-5])

# #72. Edit Distance
# def minDistance(word1, word2):
#     """
#     :type word1: str
#     :type word2: str
#     :rtype: int
#     """
#     #row - word1, coulmn - word2
#     m = len(word1)
#     n = len(word2)
#
#     D = [[0 for i in range(n+1)] for j in range(m+1)]
#
#     for i in range(1,m+1):
#         D[i][0] = i
#     for i in range(1,n+1):
#         D[0][i] = i
#
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if(word1[i-1] == word2[j-1]):
#                 D[i][j] = D[i-1][j-1]
#             else:
#                 D[i][j] = 1 + min(D[i-1][j], D[i-1][j-1], D[i][j-1])
#     return D[-1][-1]
# print minDistance("barada","annada")

# #120. Triangle
# def minimumTotal(triangle):
#     """
#     :type triangle: List[List[int]]
#     :rtype: int
#     """
#     m = len(triangle)
#     if (m == 1):
#         return triangle[0][0]
#     triangle[1][0] += triangle[0][0]
#     triangle[1][1] += triangle[0][0]
#     for i in range(2, m):
#         l = len(triangle[i])
#         triangle[i][0] += triangle[i - 1][0]
#         triangle[i][l - 1] += triangle[i - 1][l - 2]
#         for j in range(1, l - 1):
#             triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
#
#     return min(triangle[-1])
#
# print minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])

#312. Burst Balloons
#https://leetcode.com/problems/burst-balloons/discuss/76263/My-readable-Python-~500ms-accepted-solution-with-explanation
#Interval Problem like largest palindrome
#https://leetcode.com/problems/burst-balloons/discuss/76230/C++-dp-detailed-explanation
"""
With each iteration I gradually increase the interval between balloons l and r. Such process is equivalent to beginning from the 1st burst balloon.
As the interval to be considered increases,
I focus on the region (l,r), and assign m as the last balloon to be burst in this region. I need to calculate:

max coins after the balloons in region (l,m) are burst

max coins after the balloons in region (m,r) are burst

nums[l]*nums[m]*nums[r]
"""
# def maxCoins(nums):
#     nums = [1] + [n for n in nums] + [1]
#     R = [[0 for i in range(len(nums))] for j in range(len(nums))]
#     for num_ballons in range(1,len(nums)-1):
#         for l in range(1,len(nums)- num_ballons):
#             r = l + num_ballons - 1
#             for m in range(l,r+1): #the lth and rth balloons are burst in this sub-problem.
#                 R[l][r] = max(R[l][r],R[l][m-1] + nums[l-1]* nums[m]* nums[r+1] + R[m+1][r])
#         print R
#     print R
#     return R[1][-2]
# print maxCoins([3,1,5,8])

#1,3,1,5,8,1
#3 -> 3, 1 -> 15; 5 -> 40;  8 -> 40
#3,1 -> 3*1*5 + 1*3*5 = 30; 1,5 -> 3*1*5 + 3*5*8 = 135; 5,8 -> 1*5*8 + 1*8*1 = 48
#3,1,5 -> 3*1*5 + 3*5*8 + 3*8*1= 159; 1,5,8 -> 3*1*5 + 3*5*8 + 3*8*1 = 159
#3,1,5,8 -> 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167


#647. Palindromic Substrings
#https://leetcode.com/problems/palindromic-substrings/solution/
# def countSubstrings(S):
#     N = len(S)
#     ans = 0
#     for center in xrange(2 * N - 1): center can character(odd) or between two chracter(even)
#         left = center / 2
#         right = left + center % 2
#         while left >= 0 and right < N and S[left] == S[right]:
#             ans += 1
#             print S[left:right+1]
#             left -= 1
#             right += 1
#     return ans
#
# print countSubstrings("aaa")

#5. Longest Palindromic Substring
# def longestPalindrome(s): #Not DP
#     N = len(s)
#     index = 0
#     max_ = 0
#     for center in xrange(2 * N - 1):
#         left = center / 2
#         right = left + center % 2
#         while left >= 0 and right < N and s[left] == s[right]:
#             length = right - left + 1
#             if max_ < length:
#                 max_ = length
#                 index = left
#             left -= 1
#             right += 1
#     return s[index:index + max_]

#non-dp solution is better
# class Solution(object):
#     def longestPalindrome(self, s):
#         N = len(s)
#         if(N == 1):
#             return s
#         if(N==2):
#             if s[0] == s[1]:
#                 return s
#             else:
#                 return s[0]
#         max_ = 1
#         index = 0
#         R =[[0 for i in range(N)] for j in range(N)]
#         for i in range(N):
#             R[i][i] = 1
#             if i < N-1 and s[i]==s[i+1] :
#                 index = i
#                 max_ = 2
#                 R[i][i+1] = 1
#         for length in range(3,N+1):
#             for l in range(N-length + 1):
#                 r = l + length -1
#                 if(s[l] == s[r] and R[l+1][r-1]):
#                     R[l][r] = 1
#                     if max_ < length:
#                         max_ = length
#                         index = l
#         return s[index:index + max_]





s = Solution()
print s.longestPalindrome("babad")