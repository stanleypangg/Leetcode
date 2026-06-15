# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        n = len(arr)
        res = 0
        for i in range(n // 2):
            twin_sum = arr[i] + arr[n - 1 - i]
            res = max(res, twin_sum)
        
        return res