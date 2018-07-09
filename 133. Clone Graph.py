#use Map + DFS
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        node_copy = UndirectedGraphNode(node.label)#crreate instance of node
        stack = [node] #used for DFS
        Graph = {node:node_copy} #store the original node:clone node.
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in Graph:# neighbor is not visited
                    neighbor_copy = UndirectedGraphNode(neighbor.label)
                    Graph[neighbor] = neighbor_copy
                    Graph[node].neighbors.append(neighbor_copy)
                    stack.append(neighbor)
                else:
                    Graph[node].neighbors.append(Graph[neighbor])
        return node_copy





