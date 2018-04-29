#two pointer approach
class Solution(object):
    def compress(self, chars):
        write = 0
        anchor = 0
        for read,char in enumerate(chars):
            if read == len(chars)-1 or chars[read+1] != char: #Time for writing
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:#only case hen length more than 1
                    for d in str(read-anchor+1):
                        chars[write] = d
                        write += 1
                    anchor = read + 1
        return write
s  = Solution()
print s.compress(["a","a","b","b","c","c","c"])


