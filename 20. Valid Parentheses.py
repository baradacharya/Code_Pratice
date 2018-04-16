class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        for c in s:
            if(c == '('): stack.append(')')
            elif (c == '['): stack.append(']')
            elif (c == '{'): stack.append('}')
            elif (not stack or c != stack.pop()):
                return False
        return False if len(stack) > 0 else True