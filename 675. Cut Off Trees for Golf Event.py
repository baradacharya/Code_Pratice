#36 / 53 test cases passed. #TLE
class Solution(object):
    def cutOffTree(self, forest):
        def bfs(forest, sr, sc, tr, tc):
            import collections
            R, C = len(forest), len(forest[0])
            queue = collections.deque([(sr, sc, 0)])
            seen = {(sr, sc)}
            while queue:
                r, c, d = queue.popleft()
                if r == tr and c == tc:
                    return d
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (0 <= nr < R and 0 <= nc < C and
                                (nr, nc) not in seen and forest[nr][nc]):
                        seen.add((nr, nc))
                        queue.append((nr, nc, d + 1))
            return -1
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        sr = sc = ans = 0
        for _, tr, tc in trees:
            d = bfs(forest, sr, sc, tr, tc)
            if d < 0: return -1
            ans += d
            sr, sc = tr, tc
        return ans

s = Solution()
print s.cutOffTree([[1,2,3],[0,0,4],[7,6,5]])

