"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = deque([root])
        while q:
            curr_len = len(q)
            for i in range(curr_len):
                curr = q.popleft()

                if i == curr_len - 1:
                    curr.next = None
                else:
                    curr.next = q[0]
                
                if curr.left and curr.right:
                    q.append(curr.left)
                    q.append(curr.right)
        
        return root