class Solution(object):
    # def numJewelsInStones(self, J, S):
    #     """
    #     :type J: str
    #     :type S: str
    #     :rtype: int
    #     """
    #     chardict = {}
    #     for char in S:
    #         if char in chardict:
    #             chardict[char] += 1
    #         else:
    #             chardict[char] = 1
    #     res = 0
    #     for char in J:
    #         if char in chardict:
    #             res += chardict[char]
    #     return res

    def numJewelsInStones(self, J, S):
        return sum(s in J for s in S)