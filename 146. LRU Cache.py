class LinkedListNode(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next  = None
        self.prev = None

class LRUCache(object):
    #Dictionary will contain <(Key,LinkedListNode)>
    #Use Double Linkedlist, head for removal, tail for adding into the list.
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = dict()
        self.head = LinkedListNode(0,0) #dummy node, keep track of beginning
        self.tail = LinkedListNode(0,0) #dummy node, keep track of end
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        if present get the key and remove the node from list and reinsert at end
        :type key: int
        :rtype: int
        """
        if key in self.dic:#remove node from beginning and insert into end
            node = self.dic[key]
            self._remove(node) #remove the key
            self._add(node) #Add it in the tail
            return node.value
        else:
            return -1


    def put(self, key, value):
        """
        if present get the key and remove the node from list and reinsert at end
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:#remove from the list
            self._remove(self.dic[key])
        node = LinkedListNode(key,value)
        self._add(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity: #remove the first node from the list and coresponding dic entry
            del_node =  self.head.next
            self._remove(del_node)
            del self.dic[del_node.key]

    def _add(self,node):
        """
        add this node in the end
        :param node:
        :return: void
        """
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        """
        remove this node in the end
        :param node:
        :return: void
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del node



# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
cache.put(1, 1);
cache.put(2, 2);
print cache.get(1);       #returns 1
cache.put(3, 3);    #evicts key 2
print cache.get(2);       #returns -1 (not found)
cache.put(4, 4);    #evicts key 1
print cache.get(1);       #returns -1 (not found)
print cache.get(3);       #returns 3
print cache.get(4);       #returns 4