class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        word_list = []
        for word in words:
            word_list.append((len(word),word))#SORT ACCORDING TO LENGTH
        word_list.sort()
        pre_word = set()
        ans =[]
        for i in range(len(word_list)):
            if self.wordBreak(word_list[i][1],pre_word):#ONLY CHECK FOR PREVIOUS WORD
                ans.append(word_list[i][1])
            pre_word.add(word_list[i][1])
        return ans

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(wordDict) == 0: return False
        dp = [True]  # for dp[0] always true initialization
        for i in range(1, len(s) + 1):  # exclusive
            flag = False
            for j in range(i):
                # print s[j:i]
                if dp[j] and s[j:i] in wordDict:
                    flag = True
                    break
            dp.append(flag)
            # print dp
        return dp[-1]
s = Solution()
print s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])
