class Solution(object):
    #Length problem, 2D DP
    def longestPalindrome(self, s):
        N = len(s)
        if N == 1:
            return s
        if N==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]

        DP = [[0 for i in range(N)] for j in range(N)]
        max_len  = 1
        index = 0
        #put each len 1 and 2 element
        for i in range(N):
            DP[i][i] = 1
            if i < N-1 and s[i] == s[i+1]:
                max_len = 2
                index = i
                DP[i][i+1] = 1
        for length in range(3,N+1):
            #when len = N, -> i = 0 range(1), j = N-1 => N-length+1 = N-N+1 = 1
            for i in range(N-length+1):
                j = i + length - 1
                if DP[i+1][j-1] and s[i] == s[j]:
                    DP[i][j] = 1
                    max_len = length
                    index = i
        return s[index:index+max_len]


