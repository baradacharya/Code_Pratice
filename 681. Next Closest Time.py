class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            flag = False
            cur = (cur + 1) % (24 * 60)
            a = divmod(cur, 60)
            b = divmod(a[0], 10)
            for d in b:
                if d not in allowed:
                    flag = True
                    break
            if flag: continue
            c = divmod(a[1], 10)
            for d in c:
                if d not in allowed:
                    flag = True
                    break
            if flag: continue
            return "{:02d}:{:02d}".format(*divmod(cur, 60))
            # if all(digit in allowed
            #        for block in divmod(cur, 60)
            #        for digit in divmod(block, 10)):
            #     return "{:02d}:{:02d}".format(*divmod(cur, 60))
s = Solution()
print s.nextClosestTime("19:34")