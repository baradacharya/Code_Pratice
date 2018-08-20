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
            newTime = divmod(cur, 60)
            hour = divmod(newTime[0], 10)
            for d in hour:
                if d not in allowed:
                    flag = True
                    break
            if flag:
                continue
            minute = divmod(newTime[1], 10)
            for d in minute:
                if d not in allowed:
                    flag = True
                    break
            if flag:
                continue
            return "{:02d}:{:02d}".format(*divmod(cur, 60))

s = Solution()
print s.nextClosestTime("19:34")