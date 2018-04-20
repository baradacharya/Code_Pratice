class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int_pos  = pow(2,31)-1
        max_int_neg  = pow(2,31)
        neg = False
        if x < 0:
            x = -x
            neg = True
        num = 0
        for i in reversed(str(x)):
            num = num *10 + int(i)
        if neg :
            if num > max_int_neg:return 0
            else: return -1 * num
        else:
            if num > max_int_pos: return 0
            else: return num