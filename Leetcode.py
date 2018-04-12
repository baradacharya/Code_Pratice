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

# #692. Top K Frequent Words
# import collections
# import heapq
# import functools
#
# @functools.total_ordering
# class Element:
#     def __init__(self, count, word):
#         self.count = count
#         self.word = word
#
#     def __lt__(self, other):
#         if self.count == other.count:
#             return self.word > other.word
#         return self.count < other.count
#
#     def __eq__(self, other):
#         return self.count == other.count and self.word == other.word
#
#
# class Solution(object):
#     def topKFrequent(self, words, k):
#         counts = collections.Counter(words)
#
#         freqs = []
#         heapq.heapify(freqs)
#         for word, count in counts.items():
#             heapq.heappush(freqs, (Element(count, word), word))
#             if len(freqs) > k:
#                 heapq.heappop(freqs)
#
#         res = []
#         for _ in range(k):
#             res.append(heapq.heappop(freqs)[1])
#         return res[::-1]
# S = Solution()
# S.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],2)

# #56. Merge Intervals
#
# def merge(intervals):
#     intervals.sort(key = lambda l:l[0])
#
#     merged = []
#     for interval in intervals:
#         # if the list of merged intervals is empty or if the current
#         # interval does not overlap with the previous, simply append it.
#         if not merged or merged[-1][1] < interval[0]:
#             merged.append(interval)
#         else:
#             # otherwise, there is overlap, so we merge the current and previous
#             # intervals.
#             merged[-1][1] = max(merged[-1][1], interval[1])
#
#     return merged
# #
# #merge([[2,6],[8,10],[1,3],[15,18]])
# merge([[1,3],[2,6],[8,10],[15,18]])

# #347. Top K Frequent Elements
# import collections
# def topKFrequent(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: List[int]
#     """
#     # Use Counter to extract the top k frequent elements
#     # most_common(k) return a list of tuples, where the first item of the tuple is the element,
#     # and the second item of the tuple is the count
#     # Thus, the built-in zip function could be used to extract the first item from the tuples
#     counts = collections.Counter(nums)
#     n = counts.most_common(k)
#     return zip(*collections.Counter(nums).most_common(k))[0]
# l = topKFrequent([1,1,1,2,2,3],2)
# print(l)

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

# def twoSum(nums, target):
#     if len(nums) <= 1:
#         return False
#     buff_dict = {}
#     for i in range(len(nums)):
#         if nums[i] in buff_dict:
#             return [buff_dict[nums[i]], i]
#         else:
#             buff_dict[target - nums[i]] = i
# x =twoSum([3,2,4],6)

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

# DFS
# def permute(nums):
#     res = []
#     dfs(nums, [], res)
#     return res
#
#
# def dfs(nums, path, res):
#     if not nums:
#         res.append(path)
#         # return # backtracking
#     for i in xrange(len(nums)):
#         dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)
#
# res = permute([1,2,3])
# print res

# permute(char *a, int l, int r)
# {
#    int i;
#    if (l == r)
#      printf("%s\n", a);
#    else
#    {
#        for (i = l; i <= r; i++)
#        {
#           swap((a+l), (a+i));
#           permute(a, l+1, r);
#           swap((a+l), (a+i)); //backtrack
#        }
#    }
# }
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
# def decodeString( s):
#     stack = []
#     stack.append(["", 1])
#     num = ""
#     for ch in s:
#         if ch.isdigit():
#             num += ch
#         elif ch == '[':
#             stack.append(["", int(num)])
#             num = ""
#         elif ch == ']':
#             st, k = stack.pop()
#             stack[-1][0] += st * k
#         else:
#             stack[-1][0] += ch
#     return stack[0][0]
# d = decodeString("3[a]2[bc]")
# d1 = decodeString("3[a2[c]]")

#any

#79. Word Search
class solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp #backtrack
        return res

s = solution()

print s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")