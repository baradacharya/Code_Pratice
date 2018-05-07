"""
length of longest substring T that contains atmost two distinct chars
"""
#similar to 340
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        maintain two pointers and a dictionary 
        """
        distinct = {}
        l = 0 #left pointer
        max_len = 0
        for r,c in enumerate(s):#right pointer
            if len(distinct) == 2 and c not in distinct:
                #two chars alredy in dict, remove the not latest one(min index).replace with latest one
                ind = min(distinct.values()) #will get the char with lowest position index
                l = ind+1 #update left pointer
                for char in distinct:
                    if distinct[char] == ind:
                        break
                distinct.pop(char)
            distinct[c] = r #store most recent index of char
            max_len = max(max_len,r-l+1) #update max len
        return max_len
s = Solution()
s.lengthOfLongestSubstringTwoDistinct("abccdcddc")
