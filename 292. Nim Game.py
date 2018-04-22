"""
the problem description says, if there are exactly four stones in the pile, you will lose.
you have to ensure that you never reach the situation where there are exactly four stones on the pile on your turn.
if there are five, six, or seven stones you can win by taking just enough to leave four stones for your opponent so that they lose.
But if there are eight stones on the pile, you will inevitably lose,
because regardless whether you pick one, two or three stones from the pile,
your opponent can pick three, two or one stone to ensure that, again, four stones will be left to you on your turn.
"""
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0