"""
finding if a cycle exists in a directed graph
topological sort
return the ordering of courses you should take to finish all courses.
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        def DFS(i):
            if visited[i] == -1:  # being visited, cycle found
                return False
            if visited[i] == 1:  # already visited
                return True
            visited[i] = -1  # marked as being visited
            for j in graph[i]:
                if not DFS(j): return False
            visited[i] = 1  # marked as visited
            res.append(i)  # add to course seq after visited
            return True

        res = []
        possible = True
        for x, y in prerequisites:
            graph[x].append(y)
        for i in range(numCourses):
            if not visited[i]:
                if not DFS(i):
                    possible = False
                    break

        if possible == True:
            return res
        else:
            return []

s = Solution()
print s.canFinish(4, [[1,0],[2,0],[3,1],[3,2]])