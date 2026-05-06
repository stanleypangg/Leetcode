# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
            
        length = 0

        cur = head
        while cur:
            length += 1
            cur = cur.next

        k %= length
        if k == 0:
            return head 

        # then figure out where to split the array
        # iterate length - k times

        prev = None
        cur = head
        for _ in range(length - k):
            prev = cur
            cur = cur.next

        prev.next = None
        temp = cur

        while cur.next:
            cur = cur.next
        cur.next = head

        return temp