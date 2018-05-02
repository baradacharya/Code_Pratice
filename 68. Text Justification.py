"""
greedy approach
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        cur_line,res,no_char = [],[],0
        for word in words:
            #keep manadatory space between words.
            no_word = len(cur_line)
            if no_char + no_word + len(word) > maxWidth: #done with adding words for this line,adjust line space
                #adjust in cur line
                for i in range(maxWidth-no_char):#available space
                    cur_line[i%(no_word-1 or 1)] += ' ' #add spae in round robin method
                #new line
                res.append(''.join(cur_line)) #convert list to string
                cur_line,no_char = [],0
            #have space in current line
            cur_line.append(word)
            no_char += len(word)
        #the last line must be left-justified instead of fully-justified.
        cur_line = ' '.join(cur_line).ljust(maxWidth)
        res.append(cur_line)
        return res

s = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print s.fullJustify(words,maxWidth)


