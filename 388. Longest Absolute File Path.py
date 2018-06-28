class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
    def lengthLongestPath(self, input):
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name) #hierarchy depth of file, no of tab'\t'
            if '.' in name: #file
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:#directory
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen

s = Solution()
# print s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
print s.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")