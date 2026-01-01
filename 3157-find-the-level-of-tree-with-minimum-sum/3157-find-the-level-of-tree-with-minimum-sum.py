# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        res = 0
        total = float('inf')

        level = 0
        q = deque([root])
        while q:
            level += 1
            curr_total = 0
            for _ in range(len(q)):
                curr = q.popleft()
                curr_total += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if curr_total < total:
                total = curr_total
                res = level
        
        return res