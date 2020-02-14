# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        final_list = ListNode('x')
        if l1.val >= l2.val:
            final_list.next = l2
        else:
            final_list.next = l1
        while l1.next != None and l2.next != None:
            l3 = ListNode('x')
            print('l1.val={}'.format(l1.val))
            print('l2.val={}'.format(l2.val))
            if l1.val == l2.val:
                l3 = l2.next
                l2.next = l1
                l1 = l3
                l2 = l2.next.next
            elif l1.val > l2.val:
                l3 = l2.next
                l2.next = l1
                l1 = l3
                l2 = l2.next
            else:
                l3 = l1.next
                l1.next = l1
                l2 = l3
                l1 = l1.next
        