"""
Input:
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation:
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.
Each process only has one parent process, but may have one or more children processes.
"""

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        pid_map = {} #Parent : list of children
        for i,p in enumerate(ppid):
            if p in pid_map:
                pid_map[p].append(pid[i])
            else:
                pid_map[p] = list()
                pid_map[p].append(pid[i])
        killed = set()
        stack = list()
        stack.append(kill) #DFS
        while stack:
            p = stack.pop()
            if p in killed: continue
            killed.add(p)
            if p in pid_map: stack += pid_map[p]
        return list(killed)


s = Solution()
print s.killProcess([10,8,4,7,5,6,1,2,3,9],[2,7,7,2,7,7,2,0,7,7],3)