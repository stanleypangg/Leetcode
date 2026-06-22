# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None

        res = NodeCopy(root.val)
        cache = {root: res, None: None}

        def dfs(original, copied):
            if not original:
                return
            
            if original.left not in cache:
                cache[original.left] = NodeCopy(original.left.val)
            copied.left = cache[original.left]
            dfs(original.left, copied.left)

            if original.right not in cache:
                cache[original.right] = NodeCopy(original.right.val)
            copied.right = cache[original.right]
            dfs(original.right, copied.right)

            if original.random not in cache:
                cache[original.random] = NodeCopy(original.random.val)
            copied.random = cache[original.random]

        dfs(root, res)
        return res