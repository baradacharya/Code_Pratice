#Each number in candidates may only be used once in the combination.
#39
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        candidates.sort()
        self.DFS(candidates, target, 0, res, [])
        return list(res)

    def DFS(self, candidates, target, start, res, path):
        if target < 0:
            return
        if target == 0:
            res.add(tuple(path))
            return
        for i in range(start, len(candidates)):
            self.DFS(candidates, target - candidates[i], i + 1, res,
                     path + [candidates[i]])  # not i+1 as we can reuse same i.

s = Solution()
print s.combinationSum([10,1,2,7,6,1,5],8)