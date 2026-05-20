# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        cur = head
        res = head.next
        while cur and cur.next:
            nextt = cur.next
            temp = nextt.next
            nextt.next = cur
            cur.next = temp
            if prev:
                prev.next = nextt
            prev = cur
            cur = temp
        
        return res