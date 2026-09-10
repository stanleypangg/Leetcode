# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def dfs(node):
            if not node:
                return 0, 0

            nonlocal res

            t1, c1 = dfs(node.left)
            t2, c2 = dfs(node.right)

            total = t1 + t2 + node.val
            count = c1 + c2 + 1

            if total // count == node.val:
                res += 1
            
            return total, count

        dfs(root)
        return res