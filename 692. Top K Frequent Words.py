class Solution(object):
    #T: O(nlogk), freq = O(n), heapify : O(logk) in python O(N+klogN)
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        count  = Counter(words)
        heap = [(-freq, word) for word,freq in count.items()]
        import heapq
        heapq.heapify(heap) #-ve count ,because we r using min heap
        topk = []
        for i in range(k):
            topk.append(heapq.heappop(heap)[1]) #priorty queue internally sort by character
        return topk
s =Solution()
print s.topKFrequent(["i", "am", "am", "i", "love", "coding"],2)


"""
import functools

@functools.total_ordering
class Element:
    def __init__(self,word,count):
        self.word = word
        self.count = count
    def __lt__(self,other):
        if self.count == other.count:
            return self.word > other.word
        else:
            return self.count < other.count
    def __eq__(self,other):
        return self.count == other.count and self.word == other.word
        
class Solution(object):
    def topKFrequent(self, words, k):
        
        counts  = collections.Counter(words)
        freq = []
        heapq.heapify(freq)
        
        for word,count in counts.items():
            heapq.heappush(freq,(Element(word,count),word))
            
            if(len(freq) > k):
                heapq.heappop(freq)
            
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freq)[1])  
        return res[::-1]

"""