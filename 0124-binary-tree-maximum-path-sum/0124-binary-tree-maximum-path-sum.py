# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1001

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            opt_prop = max(node.val, node.val + left, node.val + right)
            opt_local = max(opt_prop, node.val + left + right)
            self.res = max(self.res, opt_local)

            return opt_prop
        
        dfs(root)
        return self.res