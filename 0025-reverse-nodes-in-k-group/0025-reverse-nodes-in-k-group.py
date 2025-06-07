# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        dummy = ListNode(0)
        dummy.next = head
        
        curr = head
        prev_tail = dummy
        for _ in range(length // k):
            group_head = curr
            prev = None
            for _ in range(k):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            prev_tail.next = prev
            group_head.next = curr
            prev_tail = group_head

        return dummy.next