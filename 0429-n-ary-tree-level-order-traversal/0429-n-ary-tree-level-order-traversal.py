"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
            
        res = []

        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                for child in curr.children:
                    if child:
                        q.append(child)
                level.append(curr.val)
            res.append(level)
        
        return res