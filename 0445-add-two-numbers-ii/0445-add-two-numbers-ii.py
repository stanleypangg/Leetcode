# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        def toArray(l):
            arr = []
            while l:
                arr.append(l.val)
                l = l.next
            return arr
        
        a1 = toArray(l1)
        a2 = toArray(l2)
        carry = 0
        head = None

        while a1 or a2 or carry:
            total = carry
            if a1:
                total += a1.pop()
            if a2:
                total += a2.pop()

            carry = total // 10
            head = ListNode(total % 10, head)
        
        return head