"""
A Disjoint Set Union DS
DSU data structure can be used to maintain knowledge of the connected components of a graph, and query for them quickly.

1. Find: which outputs a unique id so that two nodes have the same id if and only if they are in the same connected component.
2. Union:  which draws an edge (x, y) in the graph, connecting the components with id find(x) and find(y) together.

Time: takes O(n) time in worst case.
These methods can be improved to O(Logn) using Union by Rank or Height.
"""
# if parent[i] is i, it is root,otherwise root node.
# parent is disjoint set

#Detect Cycle in an Undirected Graph
class Graph(object):
    def __init__(self,vertices):
        self.V = vertices
        import collections
        self.graph = collections.defaultdict(list)
        self.p = range(self.V) #will store parent of each node

    def addEdge(self,u,v):
        self.graph[u].append(v)

    # A utility function to find the subset of an element i
    def find(self,i):
        if self.p[i] != i: #i is not root
            i = self.find(self.p[i])#find the parent
        return i

    # A utility function to do union of two subsets
    def union(self,x, y):
        self.p[self.find(x)] =self.find(y) #we can do vice-versa

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
