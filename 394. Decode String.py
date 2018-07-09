class Solution(object):
    def decodeString(self, s):
        stack = [] #regex, freq
        stack.append(["",1])
        num = ""
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(["",int(num)]) #set the frequency of this expression
                num  = "" #reset number
            elif ch == ']':
                re,k = stack.pop()
                stack[-1][0] += re * k #pop the stack and upadate the reg ex below first layer
            else:
                stack[-1][0] += ch #update the stack reg ex
        return stack[0][0]

s = Solution()
# print s.decodeString(s = "3[a]2[bc]")
print s.decodeString(s = "3[a10[c]]")


"""
[['', 1], [u'a', 3]]
[[u'aaa', 1], [u'b', 2]]
[[u'aaa', 1], [u'bc', 2]]
"""
