# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.queue = []
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while 1:
            buf4 = [""]*4
            l = read4(buf4)
            if l :
                self.queue.extend(buf4)
            read = min(len(self.queue),n-i)
            for _ in read:
                buf[i] = self.queue.pop(0)
                i += 1
            if read == 0:
                break
        return i