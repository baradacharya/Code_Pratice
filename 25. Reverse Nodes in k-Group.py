# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count  = 0
        while cur and count != k: #K+1 node
            cur,count = cur.next,count+1
        if count == k : #need to reverse
            cur = self.reverseKGroup(cur,k) #cur will store next reversed node
            while count > 0 :#to keep track at which node we should stop reversing
                count -= 1
                next_node = head.next
                head.next,cur,head = cur,head,next_node
            head = cur #final
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
b = s.create_List([1,2,3,4,5])
print s.traverse_list(b)
a = s.reverseKGroup(b,2)
print s.traverse_list(a)
