#Simple sum array on one dimension, O(n) for both update and sum
class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        #store sum array row wise : Mat[i][j] = sum(mat[i][0:j]).
        for row in matrix:
            for col in xrange(1, len(row)):
                row[col] += row[col - 1]
        self.matrix = matrix

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        #1.find the original value of that point
        original = self.matrix[row][col]
        if col > 0:
            original -= self.matrix[row][col - 1]
        #2. get the difference value from old and new
        diff = original - val

        #3. prpogate the diff from the cur col to forward up to end of this row.
        for j in xrange(col, len(self.matrix[0])):
            self.matrix[row][j] -= diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        #for the region in row cal sum
        sum = 0
        for row in xrange(row1, row2 + 1):
            sum += self.matrix[row][col2]
            if col1 > 0:
                sum -= self.matrix[row][col1 - 1]
        return sum

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
s = NumMatrix(matrix)
print s.sumRegion(2, 1, 4, 3)
s.update(3, 2, 2)
print s.sumRegion(2, 1, 4, 3)