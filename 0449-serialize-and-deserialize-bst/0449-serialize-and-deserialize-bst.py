# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []

        def preorder(node):
            if not node:
                res.append(str(-1))
                return
            
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ' '.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        parts = data.split()
        if not parts:
            return None
        
        print(parts)
        i = 0

        def preorder():
            nonlocal i
            cur = int(parts[i])

            i += 1
            if i > len(parts) or cur == -1:
                return None
            
            node = TreeNode(cur)
            node.left = preorder()
            node.right = preorder()
        
            return node
    
        return preorder()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans