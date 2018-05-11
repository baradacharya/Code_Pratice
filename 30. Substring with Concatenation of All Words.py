#dictionary
class Solution(object):
    # def findSubstring(self, s, words):
    #     """
    #     :type s: str
    #     :type words: List[str]
    #     :rtype: List[int]
    #     """
    #     if not s or not words or not words[0]:
    #         return  []
    #     n = len(s)
    #     word_len = len(words[0])
    #     total_words_len = word_len * len(words)
    #     if n < total_words_len:
    #         return []
    #     count_words = {}
    #     for word in words:
    #             count_words[word] = count_words.get(word,0) + 1
    #     ans = []
    #     i = 0
    #     while i < len(s):
    #         if self.helper(s[i:i+total_words_len],count_words,word_len):
    #             ans.append(i)
    #         i += 1
    #     return ans
    #
    # def helper(self,s,counter,word_len):
    #     i = 0
    #     dic_s = {}
    #     while i < len(s):
    #         word = s[i:i+word_len]
    #         if word in counter:
    #             dic_s[word] = dic_s.get(word,0) + 1
    #             i += word_len
    #         else:
    #             return False
    #     for word in counter:
    #         if word in dic_s:
    #             if counter[word] != dic_s[word]:
    #                 return False
    #         else:
    #             return False
    #     return True

    #Optimized approach two point dictionary approach
    def _findSubstring(self, i, n, word_len, words_len, s, words_dic, ans):
        cur_dic = {}
        l = r = i #two pointers
        while r + word_len <= n:
            word = s[r:r + word_len]
            r += word_len
            if word not in words_dic:
                l = r #update left pointer
                cur_dic.clear()
            else:
                cur_dic[word] = cur_dic[word] + 1 if word in cur_dic else 1
                #if cur_dic has more words, remove word and update left pointer till word freq matche
                while cur_dic[word] > words_dic[word]:
                    cur_dic[s[l:l + word_len]] -= 1
                    l += word_len
                if r - l == words_len:#res
                    ans.append(l)

    def findSubstring(self, s, words):
        if not s or not words or not words[0]:
            return []
        n = len(s)
        word_len = len(words[0])
        words_len = len(words) * word_len
        words_dic = {}
        for w in words:
            words_dic[w] = words_dic[w] + 1 if w in words_dic else 1
        ans = []
        #Important trick words len same,so sequence can be [0,k,2k,3k..] or [1,k+1,2k+1..]..[k-1,2k-1,3k-1,..] where k = word_len
        for i in xrange(word_len):
            self._findSubstring(i,n,word_len, words_len,s,words_dic,ans)
        return ans

s = Solution()
# print s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"])
print s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","word"])



