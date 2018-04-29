# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        odd = head
        even = evenhead = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenhead
        return head

    def create_List(self,nums):
        if not list: return None
        cur = head = ListNode(0)
        for num in nums:
            node = ListNode(num)
            cur.next = node
            cur = cur.next
        return head.next

    def traverse_list(self,list):
        while list:
            print list.val
            list = list.next

s = Solution()
p = s.create_List([1, 2, 3])
s.traverse_list(p)
q = s.oddEvenList(p)
print s.traverse_list(q)
