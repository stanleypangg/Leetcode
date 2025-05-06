# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            sum = l1.val + l2.val + carry
            curr.next = ListNode(sum % 10)
            carry = sum // 10
            
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            remaining = l1
        elif l2:
            remaining = l2
        else:
            remaining = None

        while remaining:
            sum = remaining.val + carry
            curr.next = ListNode(sum % 10)
            carry = sum // 10

            curr = curr.next
            remaining = remaining.next
        
        if carry:
            curr.next = ListNode(1)
            
        return dummy.next
