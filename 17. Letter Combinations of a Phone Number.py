class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []
        dict = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                     "9": "wxyz", "10": " "}
        res = [""]
        for d in str(digits):
            temp_res = []
            for c in dict[d]:
                for s in res:
                    temp_res.append(s+c)
            res = temp_res
        return res

s = Solution()
print s.letterCombinations(23)
