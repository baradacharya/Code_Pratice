def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    m = len(triangle)
    if (m == 1): return triangle[0][0]
    for i in range(1, m):
        l = len(triangle[i])
        triangle[i][0] += triangle[i - 1][0]
        triangle[i][l - 1] += triangle[i - 1][l - 2]
        for j in range(1, l - 1):
            triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])

    return min(triangle[-1])

print minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])