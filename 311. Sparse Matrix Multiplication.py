#Hashmap: row dictionaries will store another dic . in each dict index and number.
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.")
        C = [[0] * l for _ in range(m)]
        dict_B = {}

        # create dic of dic for B Matrix
        for i, row in enumerate(B):
            dict_B[i] = {}
            for j, num in enumerate(row):
                if num:
                    dict_B[i][j] = num

        # Multiply Matrixes
        for i, row in enumerate(A):
            for j, numA in enumerate(row):
                if numA:
                    for k, numB in dict_B[j].iteritems():
                        C[i][k] += numA * numB
        return C
s = Solution()
print s.multiply([[1,0,0],[-1,0,3]],[[7,0,0],[0,0,0],[0,0,1]])