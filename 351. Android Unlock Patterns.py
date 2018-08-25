class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.used = [False] * 9
        res = 0
        for len in range(m,n+1):
            res += self.calcPatterns(-1, len)
            for i in range(9):
                self.used[i] = False
        return res

    def calcPatterns(self,last,len):
        if len == 0:
            return 1
        sum = 0
        for i in range(9):
            if self.isValid(i, last):
                self.used[i] = True
                sum += self.calcPatterns(i, len - 1);
                self.used[i] = False
        return sum

    def isValid(self, index, last):
        if self.used[index]:
            return False
        #first digit of the pattern
        if last == -1:
            return True;
        #knight moves or adjacent cells (in a row or in a column)
        if (index + last) % 2 == 1:
            return True
        #indexes are at both end of the diagonals for example 0,8 and 2,6
        mid = (index + last)/2
        if mid == 4:
            return self.used[mid]#True if 5 cell has already used
        #adjacent cells on diagonal (0,4) (0,5) (0,7)
        if (index%3 != last%3) and (index/3 != last/3):
            return True
        #all other cells which are not adjacent
        return self.used[mid]