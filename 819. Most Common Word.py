class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        word_dict = {}
        ans,max_count = "",0
        for word in paragraph.split(' '):
            word = word.strip("!?',;.").lower()
            if word in banned: continue
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
            if word_dict[word] > max_count:
                ans, max_count = word, word_dict[word]
        return ans
s = Solution()
print s.mostCommonWord("a.",[])
