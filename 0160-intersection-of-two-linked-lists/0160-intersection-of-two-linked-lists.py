# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLength(node):
            res = 0
            curr = node
            while curr:
                res += 1
                curr = curr.next
            return res
        
        a_len, b_len = getLength(headA), getLength(headB)

        if a_len < b_len:
            small_len, big_len = a_len, b_len
            small, big = headA, headB
        else:
            small_len, big_len = b_len, a_len
            small, big = headB, headA
        
        while small_len < big_len:
            big = big.next
            big_len -= 1
        
        while small:
            if small is big:
                return small
            small = small.next
            big = big.next
        
        return None