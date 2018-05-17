#Union By Rank and Path Compression
#O(logn)
#https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/
#https://leetcode.com/articles/redundant-connection/
"""
The above union() and find() are naive and the worst case time complexity is linear.
The trees created to represent subsets can be skewed and can become like a linked list.

for o(logn)
We use two techniques to improve the run-time complexity: path compression, and union-by-rank.

The idea is to always attach smaller depth tree under the root of the deeper tree.
This technique is called union by rank.

Path compression
When find is called, traverse to root,
add coresponding node directly under root by passing all paths.

1. Path compression involves changing the x = parent[x] in the find function
to parent[x] = find(parent[x]). Basically, as we compute the correct leader for x, we should remember our calculation.

2.Union-by-rank involves distributing the workload of find across leaders evenly. Whenever we dsu.union(x, y),
we have two leaders xr, yr and we have to choose whether we want parent[x] = yr or parent[y] = xr.
We choose the leader that has a higher following to pick up a new follower.
"""
#Union by Rank, Path Compression
class Graph(object):
    def __init__(self,vertices):
        self.V = vertices
        import collections
        self.graph = collections.defaultdict(list)
        self.p = range(self.V)
        self.rank = [0] * self.V

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def find(self,i):
        if self.p[i] != i: #i is not root
            self.p[i] = self.find(self.p[i])#find the parent
        return self.p[i]

    def union(self, i,j):
        i_r, j_r = self.find(i), self.find(j)
        if self.rank[i_r] < self.rank[j_r]:
            self.p[i_r] = j_r
        elif self.rank[j_r] < self.rank[i_r]:
            self.p[j_r] = i_r
        else:
            self.p[j_r] = i_r
            self.rank[i_r] += 1

    def isCyclic(self):
        for i in self.graph:
            for j in self.graph[i]:
                x_set = self.find(i)
                y_set = self.find(j)
                if x_set == y_set:
                    return True
                self.union(x_set,y_set)

# Create a graph given in the above diagram
g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if g.isCyclic():
    print "Graph contains cycle"
else:
    print "Graph does not contain cycle "