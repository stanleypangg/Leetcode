# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        st = []
        curr = root

        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            
            count += 1
            curr = st.pop()
            if count == k:
                return curr.val
            curr = curr.right