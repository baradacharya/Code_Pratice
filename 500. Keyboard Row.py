class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c = set('zxcvbnm')

        ans  = []
        for word in words:
            w = set(word.lower())
            if a & w == w:
                ans.append(word)
                continue
            if b & w == w:
                ans.append(word)
                continue
            if c & w == w:
                ans.append(word)
                continue
        return ans
s = Solution()
s.findWords(["Hello","Alaska","Dad","Peace"])