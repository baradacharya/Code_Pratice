#Each number in candidates may only be used once in the combination.
#39
class Solution(object):
    def combinationSum(self, k, n):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.DFS(k, n, 1,res, [])
        return res

    def DFS(self, k, target, start, res, path):
        if len(path) > k:
            return
        elif len(path) == k and target == 0:
            res.append(path)
            return
        else:
            for i in range(start,10):
                self.DFS(k, target - i, i + 1, res, path + [i])  # not i+1 as we can reuse same i.

s = Solution()
print s.combinationSum(3,7)