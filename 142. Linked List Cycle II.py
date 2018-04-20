"""
L1 : the distance between the head point and entry point

L2 : the distance between the entry point and the meeting point

C : the length of the cycle

slow pointer traveled : L1 + L2 + n1 *c

fast pointer traveled : L1 + L2 + n2 *c

2 * slow = fast
2 (L1 + L2 + n1 *c)  = L1 + L2 + n2 *c
=> L1 + L2 = (n2-n1) * c
=> L1 + L2 = nc = integer (so if we start from head and the meeting point at once, will again meet at start of cycle.)
"""
def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head: return None
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: #1st part cycle detected
            #2nd part start point of cycle
            while head != slow:
                slow = slow.next
                head = head.next
            return head
    return None