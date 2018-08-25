"""
https://leetcode.com/problems/sentence-screen-fitting/discuss/90869/Python-with-explanation
https://leetcode.com/problems/sentence-screen-fitting/discuss/90845/21ms-18-lines-Java-solution
Our goal is to find the start position of the row next to the last row on the screen, which is 25 here.
Since actually it's the length of everything earlier, we can get the answer by dividing this number by the length of (non-repeated) sentence string.
"""
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        start = 0
        for i in xrange(rows):
            start += cols
            if s[start % len(s)] == ' ':
                start += 1
            else:
                while start > 0 and s[ (start - 1) % len(s) ] != ' ':
                    start -= 1
        return start/ len(s)
s = Solution()
# print s.wordsTyping(["hello","world"],2,8)
print s.wordsTyping(["a", "bcd", "e"],3,6)