# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        binary = []

        while head:
            binary.append(head.val)
            head = head.next
        
        power = len(binary) - 1
        for digit in binary:
            res += digit * 2 ** power
            power -= 1
        
        return res