# #1.Minimum Index Sum of Two Lists
# def findRestaurant( A, B):
#     Aindex = {u: i for i, u in enumerate(A)} #dictionary
#     best, ans = 1e9, []
#
#     for j, v in enumerate(B):
#         i = Aindex.get(v, 1e9)
#         if i + j < best:
#             best = i + j
#             ans = [v]
#         elif i + j == best:
#             ans.append(v)
#     return ans
# findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])

# 6.
# class Solution(object):
#     def canFinish(self, numCourses, prerequisites):
#         """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#         """
#         graph = [[] for _ in range(numCourses)]
#         visited = [0 for _ in range(numCourses)]
#         # create graph
#         for pair in prerequisites:
#             x, y = pair
#             graph[x].append(y)
#         # visit each node
#         for i in range(numCourses):
#             if not self.dfs(graph, visited, i):
#                 return False
#         return True
#
#     def dfs(self, graph, visited, i):
#         # if ith node is marked as being visited, then a cycle is found,
#         if visited[i] == -1:
#             return False
#         # if it is done visted, then do not visit again
#         if visited[i] == 1:
#             return True
#         # mark as being visited
#         visited[i] = -1
#         # visit all the neighbours
#         for j in graph[i]:
#             if not self.dfs(graph, visited, j):
#                 return False
#         # after visit all the neighbours, mark it as done visited
#         visited[i] = 1
#         return True
#
# S = Solution()
# #S.canFinish(4, [[1,0],[0,2],[1,3]])
# S.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]])

# import random
# class RandomizedSet(object):
#     def __init__(self):
#         self.nums, self.pos = [], {}
#
#     def insert(self, val):
#         if val not in self.pos:
#             self.nums.append(val)
#             self.pos[val] = len(self.nums) - 1
#             return True
#         return False
#
#     def remove(self, val):
#         if val in self.pos:
#             idx, last = self.pos[val], self.nums[-1]
#             self.nums[idx], self.pos[last] = last, idx
#             self.nums.pop();
#             self.pos.pop(val, 0)
#             return True
#         return False
#
#     def getRandom(self):
#         return self.nums[random.randint(0, len(self.nums) - 1)]
#
# randomSet =  RandomizedSet();
# randomSet.insert(1)
# randomSet.remove(2)
# randomSet.insert(2)
# randomSet.getRandom()
# randomSet.remove(1)
# randomSet.insert(2)
# randomSet.getRandom()

# def lengthOfLongestSubstring(s):
#     start = maxLength = 0
#     usedChar = {}
#
#     for i in range(len(s)):
#         if s[i] in usedChar and start <= usedChar[s[i]]:
#             start = usedChar[s[i]] + 1
#         else:
#             maxLength = max(maxLength, i - start + 1)
#
#         usedChar[s[i]] = i
#
#     return maxLength
#
# lengthOfLongestSubstring("abcabcbb")

# class Solution:
# # @param {ListNode} head
# # @return {ListNode}
#     def reverseList(self, head):
#         prev = None
#         while head:
#             curr = head
#             head = head.next
#             curr.next = prev
#             prev = curr
#         return prev

# def reverseWords(s):
#     a =s.strip()
#     b= a.split()[::-1] #::-1 reverse list
#     return " ".join(s.strip().split()[::-1])
#
# s =reverseWords("blue is sky the")
# print (s)
# def compress(chars):
#     anchor = write = 0
#     for read, c in enumerate(chars):
#         if read + 1 == len(chars) or chars[read + 1] != c:
#             chars[write] = chars[anchor]
#             write += 1
#             if read > anchor:
#                 for digit in str(read - anchor + 1):
#                     chars[write] = digit
#                     write += 1
#             anchor = read + 1
#     return write
#d = compress(["a","a","b","b","c","c","c"])
# d = compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
# print (d)