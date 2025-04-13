# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            curr, depth = queue.popleft()

            if depth >= len(res):
                res.append([])
            res[depth].append(curr.val)

            if curr.left:
                queue.append((curr.left, depth + 1))
            if curr.right:
                queue.append((curr.right, depth + 1))
        
        return res