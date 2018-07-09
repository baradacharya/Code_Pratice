class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
    def addOperators(self, num, target):
        res, self.target = [], target
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "0*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
        return res

    # keep track of future array, expression uptil now, cur expression and last expression, res
    def dfs(self, num, exp, cur, last, res):
        print exp
        if not num:
            if cur == self.target:
                res.append(exp)
            return
        for i in range(1, len(num)+1): #num[:1] means num[0]
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "0*" as a number
                self.dfs(num[i:], exp + "+" + val, cur+int(val), int(val), res)
                self.dfs(num[i:], exp + "-" + val, cur-int(val), -int(val), res)
                self.dfs(num[i:], exp + "*" + val, cur-last+last*int(val), last*int(val), res)
                # cur = 4+2 ,last = 2, val = 5 ,we have to do 4+2*5 then cur - last + last * val = 4+2 - 2 + 2 *



s = Solution()
print s.addOperators(num = "232", target = 8)
print s.addOperators(num="105",target=5)
print s.addOperators(num="1234",target=11)
# "105", 5 #why this is required if i == 1 or (i > 1 and num[0] != "0"): required
# Output:
# ["1*0+5", "1*05", "10-5"]
# Expected:
# ["1*0+5", "10-5"]
#Output:000 0
# ["0+0+0","0+0-0","0+0*0","0-0+0","0-0-0","0-0*0","0*0+0","0*0-0","0*0*0","00+0","00-0","00*0","000"]
# Expected:
# ["0*0*0","0*0+0","0*0-0","0+0*0","0+0+0","0+0-0","0-0*0","0-0+0","0-0-0"]
# class Solution(object):
#     def addOperators(self, num, target):
#         """
#         :type num: str
#         :type target: int
#         :rtype: List[str]
#         """
#         res = []
#         self.target = target
#         for i in range(1,len(num)+ 1):
#             if i == 1 or (i > 1 and num[0]!= '0'):
#                 self.dfs(num[i:],num[:i],int(num[:i]),int(num[:i]),res)
#         return res
#     #keep track of future array, expression uptil now, cur expression and last expression, res
#     def dfs(self,num,exp,cur_value,last_value,res):
#         if not num:
#             if cur_value == self.target:
#                 res.append(exp)
#             return
#
#         for i in range(1,len(num)+1):
#             val = num[:i]
#             if i == 1 or (i > 1 and num[0] != '0'):
#                 self.dfs(num[i:], exp + "+" + val, cur_value + int(val), int(val),res)
#                 self.dfs(num[i:], exp + "-" + val, cur_value - int(val), -int(val), res)
#                 self.dfs(num[i:], exp + "*" + val, cur_value - last_value + last_value * int(val), last_value * int(val), res)
#                 # cur = 4+2 ,last = 2, val = 5 ,we have to do 4+2*5 then cur - last + last * val = 4+2 - 2 + 2 * 5

