##1: backtrack T:O(2^2n*n)
##2: Backtracking + prechecking 2nCn * 1/n+1


class Solution(object):
    ## 1.backtrack
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(s = ''):
            if len(s) == 2 * n:
                if valid(s):
                    ans.append(s)
                    return
            else:
                generate(s +'(')
                generate(s +')')

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0
        ans = []
        generate()
        return ans

    #2.backtrack + prechecking
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def generate(s = '',open = 0,close = 0):
            if len(s) == 2*n:
                ans.append(s)
                return
            else:
                if open < n:
                    generate(s+'(',open+1,close)
                if close < open:
                    generate(s+')',open,close+1)
        generate()
        return ans
s = Solution()
print s.generateParenthesis(3)
