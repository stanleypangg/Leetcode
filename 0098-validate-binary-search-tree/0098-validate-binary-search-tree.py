# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min, max):
            if not node:
                return True
            
            if min < node.val < max:
                return validate(node.left, min, node.val) and validate(node.right, node.val, max)
            else:
                return False
        
        return validate(root, float('-inf'), float('inf'))