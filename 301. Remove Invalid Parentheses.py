#https://leetcode.com/problems/remove-invalid-parentheses/discuss/75032/Share-my-Java-BFS-solution
#BFS : Always guarantee with min changes
#One level : remove one ch and check validity
#if found valid ones on the current level, put them to the final result list and we are done,
#otherwise, add them to a queue and carry on to the next level.
#In BFS we handle the states level by level, in the worst case, we need to handle all the levels,
#we can analyze the time complexity level by level and add them up to get the final complexity.
#T(n) = n * C(n)(first_level)+(n-1)*C(n-1)+  .. +1*C(1) = n 2 ^n-1
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        visited =set()
        queue = [s]
        visited.add(s)
        found  = False
        while queue:
            s = queue.pop(0)
            if self.isvalid(s):#found an answer, add to the result
                res.append(s)
                found = True
            if found : continue #no need to go to next level and generate again

            #generate all possible states
            for i in range(len(s)):
                #we only try to remove left or right parenthesis
                if s[i] != '(' and s[i] != ')':
                    continue
                new_s = s[:i] + s[i+1:]
                if new_s not in visited:
                    queue.append(new_s)
                    visited.add(new_s)
        return res

    def isvalid(self,s):
        count  = 0
        for c in s:
            if c == '(': count += 1
            if c == ')': count -= 1
            if count < 0: return False
        return count == 0



s = Solution()
print s.removeInvalidParentheses("()())()")
