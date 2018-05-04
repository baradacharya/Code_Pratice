#Idea is to get the prefix word then break the string and pass the rest of the string to a recursive function.
#store word in m/m to avoid recalculation(optional)(memory)(without it TLE will occured)(imp concept)
class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memory):
        if s in memory: return memory[s] # if we calculated earlier return result to save time
        if not s:
            return []
        res = []
        for word in wordDict:#Test for each word
            if not s.startswith(word):#for finding prefix
                continue
            if len(s) == len(word):
                res.append(word)
            else:
                restofTheString = self.helper(s[len(word):],wordDict,memory)  #return list of possible answers
                for w in restofTheString:
                    w = word + " " + w
                    res.append(w)
        memory[s] = res #add answ for a string to mem to avoid recalculation(Dic of Lists)
        return res