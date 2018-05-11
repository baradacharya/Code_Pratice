#similar as 210. Course Schedule II
#main challenge is to build the graph.
# lexographical sorted words. so compare word by word and add
#abc,ade => b->d , wrt,wrf => t-f
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        import collections
        graph = collections.defaultdict(set)

        visited = {}
        # 1. build graph: important part
        for i in range(len(words)):
            for c in words[i]: visited[c] = 0
            if i > 0:
                minlen = min(len(words[i - 1]), len(words[i]))
                for j in range(minlen):
                    if words[i - 1][j] != words[i][j]:
                        graph[words[i - 1][j]].add(words[i][j])
                        break

        possible = True
        res = []
        # 2. perform DFS to check topological dependancy and assign sequence
        for c in visited:
            if not visited[c]:
                if not self.DFS(graph, c, visited, res):
                    possible = False
                    break
        if possible == True:
            res.reverse()
            return ''.join(res)
        else:
            return ""

    def DFS(self, graph, c, visited, res):
        if visited[c] == -1: return False #being visited, cycle detected
        if visited[c] == 1: return True #already visited
        visited[c] = -1 #being visited
        if c in graph:
            for adj in graph[c]:
                if not self.DFS(graph, adj, visited, res):
                    return False
        visited[c] = 1 #mark visited
        res.append(c) #add to sequence
        return True

s =Solution()
# print s.alienOrder(["wrt","wrf","er","ett","rftt"])
# print s.alienOrder(["ab","adc"])