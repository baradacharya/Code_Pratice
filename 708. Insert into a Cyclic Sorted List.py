
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            head = Node(insertVal,None)
            head.next = head
            return head

        prev = head
        nextNode = head.next
        inserted = False
        while True:
            if (prev.val <= insertVal <= nextNode.val) \
                    or (prev.val > nextNode.val and insertVal < nextNode.val) \
                    or (prev.val > nextNode.val and insertVal > prev.val): #minnimum, maximum

                newNode = Node(insertVal,nextNode)
                prev.next = newNode
                inserted = True
                break

            prev = prev.next
            nextNode = nextNode.next
            if prev == head:
                break
        if not inserted:
            prev.next = Node(insertVal, nextNode)
        return head

for n in range(2,6,2):
    print n