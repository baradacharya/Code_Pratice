#use four pointer
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix: return res
        rowbeg,rowend,colbeg,colend = 0,len(matrix)-1,0,len(matrix[0])-1
        while rowbeg <= rowend and colbeg <= colend:
            #Move Right
            for i in range(colbeg,colend+1):
                res.append(matrix[rowbeg][i])
            rowbeg += 1
            #Move down
            for i in range(rowbeg,rowend+1):
                res.append(matrix[i][colend])
            colend -= 1
            #Move Left
            if rowbeg<= rowend:#Trick here check this condition
                for i in range(colend,colbeg-1,-1):
                    res.append(matrix[rowend][i])
            rowend -= 1
            # Move Up
            if colbeg<= colend:
                for i in range(rowend,rowbeg-1,-1):
                    res.append(matrix[i][colbeg])
            colbeg += 1
        return res

s = Solution()
print s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


