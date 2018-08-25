class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combs = []
        self.DFS(combs,[],1,n,k)
        return combs

    def DFS(self,combs,comb,start,n,k):
        if k == 0:
            combs.append(comb)
            return
        for i in range(start,n+1):
            self.DFS(combs,comb +[i],i+1,n,k-1)

s = Solution()
print s.combine(4,2)