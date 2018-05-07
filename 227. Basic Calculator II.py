class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        stack,num,sign = [],0,'+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and s[i]!= ' ') or i == len(s)-1: #last element or +,-,*,/
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    #-3/2 = -2, so take care
                    n = stack.pop()
                    if n < 0:
                        n = abs(n)/num
                        stack.append(-n)
                    else:
                        stack.append(n/num)
                sign = s[i]
                num = 0
        return sum(stack)
s = Solution()
print s.calculate("14-3/2")