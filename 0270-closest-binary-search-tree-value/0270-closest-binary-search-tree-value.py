# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.res = root.val

        def dfs(node):
            if not node:
                return
            
            curr_dist = abs(node.val - target)
            best_dist = abs(self.res - target)

            if curr_dist < best_dist:
                self.res = node.val
            elif curr_dist == best_dist:
                self.res = min(self.res, node.val)

            if node.val == target:
                return
            elif node.val < target:
                dfs(node.right)
            else:
                dfs(node.left)
        
        dfs(root)
        return self.res