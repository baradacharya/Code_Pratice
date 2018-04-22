class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i,j = 0,len(s)-1
        l = list(s)
        while i < j:
            l[i],l[j] = l[j],l[i]
            i += 1
            j -= 1
        # return s
        # l  = [i for i in s]
        # l.reverse()
        return ''.join(l)