class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = [ ]
        import collections
        dic = collections.defaultdict(list)
        if not matrix: return result
        # Step 1: Numbers are grouped by the diagonals.
        # Numbers in same diagonal have same value of row+col
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dic[i+j+1].append(matrix[i][j]) # starting indices from 1, hence i+j+1.
        # Step 2: Place diagonals in the result list.
        # But remember to reverse numbers in odd diagonals.
        for ind, valueList in dic.iteritems():
            if ind%2==1: dic[ind].reverse()
            result += dic[ind]
        return result