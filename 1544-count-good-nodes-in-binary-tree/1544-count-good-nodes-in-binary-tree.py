# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(curr, maxx):
            if not curr:
                return
            elif curr.val >= maxx:
                self.res += 1
                maxx = curr.val
            dfs(curr.left, maxx)
            dfs(curr.right, maxx)
        
        dfs(root, float('-inf'))
        return self.res