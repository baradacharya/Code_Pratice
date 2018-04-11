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