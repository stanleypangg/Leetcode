# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # O(n) time and space
        # traverse linked list, add prev pointer 
        # do is palindrome

        # how to do O(1) space?
        # flip pointers?
        
        # go halfway
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow now points to mid point
        # reverse second half of linked list
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left, right = head, prev
        
        # now, right half of list points in reverse
        # slow now points at tail
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True