"""
The idea is pretty simple. If we look at the order we can find out we just keep adding digit from 0 to 9 to every digit and make it a tree.
Then we visit every node in pre-order.
       1        2        3    ...
      /\        /\       /\
   10 ...19  20...29  30...39   ....
"""
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res  = []
        #build tree for each digit 1,2,3,..
        for i in range(1,10):
            self.DFS(i,n,res)
        return res

    def DFS(self,cur,n,res):
        if cur > n :
            return
        res.append(cur)
        for i in range(10):
            #don't change cur here because it is call by value
            if cur * 10 + i > n:
                return
            self.DFS(cur * 10 + i,n,res)

s = Solution()
print s.lexicalOrder(13)


