# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        path = []
        def dfs(node):
            if not node.left and not node.right:
                res.append('->'.join(path + [str(node.val)]))
                return
            
            if node.left:
                path.append(str(node.val))
                dfs(node.left)
                path.pop()
            if node.right:
                path.append(str(node.val))
                dfs(node.right)
                path.pop()
        
        dfs(root)
        return res