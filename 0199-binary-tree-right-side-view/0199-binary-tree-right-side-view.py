# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        queue = deque()
        queue.append(root)
        depth = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if depth == len(res):
                    res.append(curr.val)
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            depth += 1
            
        return res