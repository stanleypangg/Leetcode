# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = root

        small = p if p.val < q.val else q
        big = p if p.val > q.val else q
        
        def search(root):
            if (small.val < root.val < big.val or
                big.val == root.val or
                small.val == root.val):
                self.res = root
                return
            elif big.val < root.val:
                search(root.left)
            elif small.val > root.val:
                search(root.right)
        
        search(root)

        return self.res