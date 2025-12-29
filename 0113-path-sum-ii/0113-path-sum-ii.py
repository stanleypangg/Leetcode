# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        path = [root.val]

        def dfs(total, node):
            if not node.left and not node.right:
                if total == targetSum:
                    res.append(path.copy())
                return
            
            if node.left:
                path.append(node.left.val)
                dfs(total + node.left.val, node.left)
                path.pop()
            
            if node.right:
                path.append(node.right.val)
                dfs(total + node.right.val, node.right)
                path.pop()
        
        dfs(root.val, root)
        return res