#Trie + DFS
#https://leetcode.com/problems/word-squares/discuss/91333/Explained.-My-Java-solution-using-Trie-126ms-1616

"""
In order for this to work, we need to fast retrieve all the words with a given prefix. There could be 2 ways doing this:

Using a hashtable, key is prefix, value is a list of words with that prefix.
Trie, we store a list of words with the prefix on each trie node.
The implemented below uses hastable.
"""
#https://leetcode.com/problems/word-squares/discuss/91344/Short-PythonC++-solution
import collections
class Solution(object):
    def wordSquares(self, words):
        n = len(words[0])
        
        #Building dictionary of prefixes
        prefixDict = collections.defaultdict(list)
        for word in words:
            for i in range(1,n):
                prefixDict[word[:i]].append(word)
        print prefixDict

        def build(square):
            print ("square: ",square)
            if len(square) == n:#perfect square found
                squares.append(square)
                return
            prefix = ''.join(zip(*square)[len(square)])
            prefixList= prefixDict[prefix]
            print ("prefix: ",prefix)
            print ("prefixList : ",prefixList)
            #Check DFS
            for word in prefixList:
                build(square + [word])
        squares = []
        for word in words:
            build([word])
        return squares
s = Solution()
# print s.wordSquares(["area","lead","wall","lady","ball"])
print s.wordSquares(["abat","baba","atan","atal"]) #see DFS