class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def create_List(nums):
    if not list: return None
    cur = head = ListNode(0)
    for num in nums:
        node = ListNode(num)
        cur.next = node
        cur = cur.next
    return head.next

def traverse_list(list):
    while list:
        print list.val
        list = list.next

p = create_List([1,2,3,4])
traverse_list(p)
