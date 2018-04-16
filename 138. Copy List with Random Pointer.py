# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None

        list_dict  = {}
        node = head
        #copy nodes of linkedlist
        while node != None:
            list_dict[node] = RandomListNode(node.label)
            node = node.next
        #assign next and random pointers
        for node in list_dict:
            if node.next:
                list_dict[node].next = list_dict[node.next]
            if node.random:
                list_dict[node].random = list_dict[node.random]
            node = node.next
        return list_dict[head]
