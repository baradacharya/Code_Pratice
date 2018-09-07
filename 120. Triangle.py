def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    if not triangle:
        return
    for i in xrange(1, len(triangle)):
        for j in xrange(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
    return min(triangle[-1])

print minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])