'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.

'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time Complexity : Linear | O(n)
        Space Complexity : Constant | O(1)'''

        dummy = ListNode()
        cur = dummy
        

        while (list1 and list2):
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        
        return dummy.next