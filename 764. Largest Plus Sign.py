#2: Dynamic Programming
"""
For each (cardinal) direction, and for each coordinate (r, c)
let's compute the count of that coordinate: the longest line of '1's starting from (r, c)
and going in that direction. With dynamic programming, it is either 0 if grid[r][c] is zero,
else it is 1 plus the count of the coordinate in the same direction. For example,
if the direction is left and we have a row like 01110110,
the corresponding count values are 01230120, and the integers are either 1 more than their successor,
or 0. For each square, we want dp[r][c] to end up being the minimum of the 4 possible counts.
At the end, we take the maximum value in dp.
"""
class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in xrange(N)]
        ans = 0

        for r in xrange(N):
            count = 0
            for c in xrange(N):#left to right
                if (r, c) in banned:
                    count = 0
                else:
                    count += 1
                dp[r][c] = count

            count = 0
            for c in xrange(N - 1, -1, -1):#right to left
                if (r, c) in banned:
                    count = 0
                else:
                    count += 1

                if count < dp[r][c]:
                    dp[r][c] = count#keep the min. one

        for c in xrange(N):
            count = 0
            for r in xrange(N):#up-down
                if (r, c) in banned:
                    count = 0
                else:
                    count += 1

                if count < dp[r][c]:
                    dp[r][c] = count

            count = 0
            for r in xrange(N - 1, -1, -1):#down-up
                if (r, c) in banned:
                    count = 0
                else:
                    count += 1
                if count < dp[r][c]:
                    dp[r][c] = count
                if dp[r][c] > ans:
                    ans = dp[r][c]

        return ans
s = Solution()
print s.orderOfLargestPlusSign(5,[[4,2]])