class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]: #IX,IV,IL,IC,ID,IM
                result -= roman[s[i]]
            else:#normal case XII,XV
                result += roman[s[i]]
        return result + roman[s[-1]]

s = Solution()
print s.romanToInt("XII")
print s.romanToInt("IV")
print s.romanToInt("IX")
print s.romanToInt("LVIII")
print s.romanToInt("MCMXCIV")



