# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level = 0
        heap = []
        q = deque([root])

        while q:
            level += 1
            total = 0
            for _ in range(len(q)):
                curr = q.popleft()
                total += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if len(heap) < k:
                heapq.heappush(heap, total)
            else:
                heapq.heappushpop(heap, total)

        if len(heap) < k:
            return -1
            
        return heap[0]