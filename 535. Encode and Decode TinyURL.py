import random
import string
class Codec:
    def __init__(self):
        self.alphabet = string.ascii_letters + '0123456789' #62
        self.url2code  = {}
        self.code2url = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        code = ''.join(random.choice(self.alphabet) for _ in range(6)) #62^6
        if longUrl not in self.url2code:
            self.url2code[longUrl] = code
            self.code2url[code] = longUrl

        return 'http://tinyurl.com/' + str(self.url2code[longUrl])

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]



# Your Codec object will be instantiated and called as such:
codec = Codec()
url = 'https://leetcode.com/problems/design-tinyurl'
print codec.decode(codec.encode(url))