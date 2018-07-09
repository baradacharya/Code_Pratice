#https://leetcode.com/problems/exclusive-time-of-functions/solution/
#stack
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        res = [0] * n
        s = logs[0].split(":")
        stack.append(int(s[0]))
        i = 1
        prev = int(s[2]) #previous time step pointer
        while i <len(logs):
            s = logs[i].split(":")
            if s[1] == "start":
                if stack:
                    res[stack[-1]] += int(s[2]) - prev #cur time step not included
                stack.append(int(s[0]))
                prev = int(s[2])
            else:
                res[stack[-1]] += int(s[2]) - prev + 1 #cur time step  included
                stack.pop()
                prev = int(s[2]) + 1
            i += 1
        return res

s = Solution()
print s.exclusiveTime(3,["0:start:0","1:start:2","1:end:5","2:start:6","2:end:9","0:end:12"])