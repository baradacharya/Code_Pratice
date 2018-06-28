# #Union-Find (naive)
# class DSU(object):
#     def __init__(self):
#         self.p = range(1001)
#
#     def find(self,x):
#         if self.p[x]!= x:
#             self.p[x] = self.find(self.p[x])
#         return self.p[x]
#
#     def union(self,x,y):
#         self.p[self.find(x)] = self.find(y)

#Union-Find (Path compression, Union By Rank)
class DSU(object):
    def __init__(self):
        self.p = range(1001)
        self.rank = [0] * 1001

    def find(self,x):
        if self.p[x]!= x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self,x,y):
        x_r,y_r = self.find(x),self.find(y)
        if self.rank[x_r] < self.rank[y_r]:
            self.p[x_r] = y_r
        elif self.rank[y_r] < self.rank[x_r]:
            self.p[y_r] = x_r
        else:
            self.p[y_r] = x_r
            self.rank[x_r] += 1

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dsu = DSU()
        for u,v in edges:
            u_set = dsu.find(u)
            v_set = dsu.find(v)
            if u_set == v_set:
                return u,v
            dsu.union(u_set,v_set)

