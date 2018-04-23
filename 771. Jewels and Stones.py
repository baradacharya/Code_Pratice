class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # import collections
        # count = collections.Counter(S)
        # res = 0
        # for c in J:
        #     res += count[c]
        # return res

    def numJewelsInStones(self, J, S):
        return sum(s in J for s in S)