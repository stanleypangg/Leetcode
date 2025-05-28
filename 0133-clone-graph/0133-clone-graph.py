"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hashmap = {}

        def dfs(node):
            if node in hashmap:
                return hashmap[node]
             
            cpy = Node(node.val)
            hashmap[node] = cpy
            for n in node.neighbors:
                cpy.neighbors.append(dfs(n))
            return cpy
        
        return dfs(node)