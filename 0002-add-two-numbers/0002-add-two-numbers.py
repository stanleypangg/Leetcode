# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 and l2:
            summ = l1.val + l2.val + carry
            carry = summ // 10
            ones = summ % 10

            curr.next = ListNode(ones)

            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        remainder = None
        if l1:
            remainder = l1
        if l2:
            remainder = l2
        
        while remainder or carry:
            summ = carry
            if remainder:
                summ += remainder.val

            carry = summ // 10
            ones = summ % 10

            curr.next = ListNode(ones)

            curr = curr.next
            if remainder:
                remainder = remainder.next
            
        return dummy.next