class Solution(object):
    #1-D DP, O(N^2)
    def wordBreak(self, s, wordDict):
        # DP  = [True]
        # for i in range(1,len(s)+1):
        #     DP.append(any(DP[j] and s[j:i] in wordDict for j in range(i)))
        # return DP[-1]

        DP = [True]
        #i will be used as exlusive like s[j:i] so s[:len(s)]
        for i in range(1, len(s) + 1):
            for j in range(i):
                temp = False
                if DP[j] and s[j:i] in wordDict:
                    temp = True
                    break
            DP.append(temp)
        return DP[-1]

