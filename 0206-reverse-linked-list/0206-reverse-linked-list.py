# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy.next

        while head:
            temp = head
            head = head.next
            temp_curr = curr
            curr = temp
            curr.next = temp_curr

        return curr
