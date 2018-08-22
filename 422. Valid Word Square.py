class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        length = len(words)
        for i in range(len(words)):
            wordLen = len(words[i])
            if wordLen > length:
                return False
            if wordLen < length:
                words[i] += ' ' * (length - wordLen)

        return words == map(''.join, zip(*words))
s = Solution()
print s.validWordSquare(["abcd","bnrt","crm","dt"])