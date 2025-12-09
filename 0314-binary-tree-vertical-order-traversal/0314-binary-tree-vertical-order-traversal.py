# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # traverse entire tree for O(n) time
        # how to output sorted list?
        if not root:
            return []

        leftmost = rightmost = 0
        res = defaultdict(list)

        q = deque([(root, 0)])
        while q:
            node, x_pos = q.popleft()

            res[x_pos].append(node.val)

            leftmost = min(leftmost, x_pos)
            rightmost = max(rightmost, x_pos)
            
            if node.left:
                q.append((node.left, x_pos - 1))
            if node.right:
                q.append((node.right, x_pos + 1))
    
        return [res[i] for i in range(leftmost, rightmost + 1)]