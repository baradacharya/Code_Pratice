"""
When the cache reaches its capacity, it should invalidate
the least frequently used item before inserting a new item.
two or more keys that have the same frequency, the least recently used key would be evicted.
"""


class ListNode(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

    def connect(self, nextNode):
        self.next = nextNode
        nextNode.prev = self


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = ListNode(None, None)  # dummy node, keep track of beginning
        self.tail = ListNode(None, None)  # dummy node, keep track of end
        # Two hashmap
        # 1. Use to record the least recent Node for this count number will be on front.(LRU)
        self.count = {0: self.tail}  # key: count value:ListNode
        self.freq = {None: [self.tail, 0]}  # key: key , value:[ListNode, visit count]

        self.head.connect(self.tail)

    def move(self, key):
        node, count_ = self.freq[key]
        self.add('temp', node.val, count_ + 1)
        self.remove(key)
        self.freq[key] = self.freq['temp']
        self.freq[key][0].key = key
        del self.freq['temp']

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.freq:
            return -1
        self.move(key)
        return self.freq[key][0].val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        if key in self.freq:  # already key exists
            self.freq[key][0].val = value
            self.move(key)
            return
        if len(self.freq) > self.capacity:
            self.remove(self.tail.prev.key)
        self.add(key, value, 0)  # new key

    def add(self, key, value, count_):
        if count_ in self.count:  # already this freq count exists
            loc = self.count[count_]
        else:
            loc = self.count[count_ - 1]  # pick previous freq count
        node = ListNode(key, value)
        # loc_prev,node,loc
        loc.prev.connect(node)
        node.connect(loc)
        self.count[count_] = node
        self.freq[key] = [node, count_]

    def remove(self, key):
        node, count_ = self.freq[key]
        if self.count[count_] != node:  # not the first node of this freq,others exist
            node.prev.connect(node.next)
        elif self.freq[node.next.key][1] == count_:  # the first node of this freq
            node.prev.connect(node.next)
            self.count[count_] = self.count[count_].next
        else:  # only node of this freq
            node.prev.connect(node.next)
            del self.count[count_]
        del self.freq[key]



# Your LFUCache object will be instantiated and called as such:
cache =  LFUCache( 2 )

cache.put(1, 1)
cache.put(2, 2)
print cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
print cache.get(2)       # returns -1 (not found)
print cache.get(3)       # returns 3.
cache.put(4, 4)    # evicts key 1.
print cache.get(1)       # returns -1 (not found)
print cache.get(3)       # returns 3
print cache.get(4)       # returns 4