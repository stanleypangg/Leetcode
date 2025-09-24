# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.par = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # store ancestors in each node?
        # can early return when both nodes visited
        root.par = None
        
        def dfs(node):
            # store direct parent in each node
            if node.left:
                node.left.par = node
                dfs(node.left)
            if node.right:
                node.right.par = node
                dfs(node.right)
        
        dfs(root)

        # now p and q should have parents
        # travel up parents to generate list of ancestors
        p_ances = []
        curr = p
        while curr:
            p_ances.append(curr)
            curr = curr.par
        
        q_ances = []
        curr = q
        while curr:
            q_ances.append(curr)
            curr = curr.par
        
        # find rightmost parent
        # since its reversed, we find leftmost common
        if len(p_ances) < len(q_ances):
            # pick shorter ances chain to go up
            small, big = p_ances, q_ances
        else:
            small, big = q_ances, p_ances
        
        big = set(big)
        for node in small:
            if node in big:
                return node