# class Solution(object):
#     def nextClosestTime(self, time):
#
#         #convert into mintues
#         cur_time = 60 * int(time[:2]) + int(time[3:])
#
#         digit_set = set()
#         for t in time:
#             if t != ':':
#                 digit_set.add(int(t))
#
#         #simulate backward to check previous times
#         while True:
#             cur_time = (cur_time - 1) % (24 * 60)
#             if all(digit in digit_set
#                     for block in divmod(cur_time, 60)
#                     for digit in divmod(block, 10)):
#                 return "{:02d}:{:02d}".format(*divmod(cur_time, 60))
#
#
# s = Solution()
# print s.nextClosestTime("11:13")
# print s.nextClosestTime("11:01")
# print s.nextClosestTime("22:22")
#
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K, M):
    # write your code in Python 3.6
    groups = [[A[0],A[0]]]
    for num in A:
        for i in range(len(groups)):
            if i == 0:
                if num < groups[0][0]:
                    groups[0][0] = num
            if i+1 < len(groups) and num == groups[i][1] + 1 and num == groups[i+1][1] - 1:
                    groups[i][1] = groups[i][1] + 1








