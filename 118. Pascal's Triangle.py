class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle  =[]
        for i in range(numRows):
            row = [None for _ in range(i+1)]
            row[0],row[-1] = 1,1
            for j in range(1,len(row)-1):
                row[j] = triangle[-1][j-1] + triangle[-1][j]
            triangle.append(row)
        return triangle