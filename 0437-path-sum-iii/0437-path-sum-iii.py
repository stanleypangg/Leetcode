# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
            
        self.res = 0
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(total, node):            
            self.res += prefix[total - targetSum]
            
            prefix[total] += 1

            if node.left:
                dfs(total + node.left.val, node.left)
            if node.right:
                dfs(total + node.right.val, node.right)
            
            prefix[total] -= 1
        
        dfs(root.val, root)
        return self.res