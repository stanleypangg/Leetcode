# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head

        for _ in range(k - 1):
            first = first.next
        
        a = first
        b = head
        while first.next:
            first = first.next
            b = b.next
        
        a.val, b.val = b.val, a.val
        return head