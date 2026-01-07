# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = res = 1
        max_total = float('-inf')
        q = deque([root])
        while q:
            total = 0
            for _ in range(len(q)):
                curr = q.popleft()
                total += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if max_total < total:
                max_total = total
                res = level
            level += 1
        return res