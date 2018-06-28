class Solution(object):
    def __init__(self):
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                           "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        res = ""
        i = 0
        while num != 0:
            if num % 1000:
                res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num /= 1000
            i += 1
        return res.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num / 10] + " " + self.helper(num % 10)
        else:
            return self.lessThan20[num / 100] + " Hundred " + self.helper(num % 100)


s = Solution()
# print s.numberToWords(123)
# print s.numberToWords(12345)
print s.numberToWords(1234567)
