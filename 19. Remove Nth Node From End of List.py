# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = ListNode(0)
        node.next = head
        cur,del_node = node,node
        while n >= 0:
            cur = cur.next
            n -= 1
        while cur :
            cur,del_node = cur.next,del_node.next
        del_node.next = del_node.next.next
        return node.next