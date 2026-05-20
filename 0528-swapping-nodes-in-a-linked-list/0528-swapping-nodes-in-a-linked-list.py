# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        if k == n - k + 1:
            return head
        
        cur = head
        for i in range(max(k, n - k + 1)):
            idx = i + 1
            if idx == k:
                a = cur
            elif idx == n - k + 1:
                b = cur
            cur = cur.next

        a.val, b.val = b.val, a.val
        return head