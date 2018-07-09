"""
 There're 3 possibilities to satisfy one edit distance apart:
1) Replace 1 char:
 	  s: a B c
 	  t: a D c
2) Delete 1 char from s:
	  s: a D  b c
	  t: a    b c
3) Delete 1 char from t
	  s: a   b c
	  t: a D b c
 """
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t : return False
        if abs(len(s)-len(t)) >= 2:
            return False
        for i in range(min(len(s),len(t))):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:] #Replace 1 char:
                elif len(s) > len(t):
                    return s[i+1:] == t[i:] #Delete 1 char from s:
                else:
                    return s[i:] == t[i+1:]#Delete 1 char from t
        return True
s = Solution()
print s.isOneEditDistance("ab","acb")
print s.isOneEditDistance("cab","ad")
print s.isOneEditDistance("1203","1213")

