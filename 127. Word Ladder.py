#BFS Problem
class Solution(object):
    # #1. simple correct soln but TLE  29 / 39,changing wordList to set do the job.
    # def ladderLength(self, beginWord, endWord, wordList):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordList: List[str]
    #     :rtype: int
    #     """
    #     wordList = set(wordList)
    #     if endWord not in wordList: return 0
    #     import collections
    #     queue = collections.deque([[beginWord,1]])
    #     while queue:
    #         word,dist = queue.popleft()
    #         if word == endWord: return dist
    #         for i in range(len(word)):
    #             #Try for each word
    #             for c in "abcdefghijklmnopqrstuvwxyz":
    #                 next_word = word[:i]+c+word[i+1:]
    #                 if next_word in wordList:Dil Hai Tumhaara
    #                     wordList.remove(next_word)
    #                     queue.append((next_word,dist+1))
    #     return 0

    #2.construct neighbour dict first, preprocesses #normal BFS #improve time complexity
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def construct_dict(word_list):
            d = {} #
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
        def bfs(beginWord,endWord,d):
            import collections
            queue = collections.deque([[beginWord,1]])
            visited = set()
            while queue:
                word,dist =queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == endWord:
                        return dist
                    for i in range(len(word)):
                        w = word[:i] + '_' + word[i+1:]
                        neighbour_words = d.get(w,[])
                        for neighbour in neighbour_words:
                            queue.append((neighbour,dist+1))
            return 0

        d = construct_dict(set(wordList))
        return bfs(beginWord,endWord,d)

s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print s.ladderLength(beginWord,endWord,wordList)