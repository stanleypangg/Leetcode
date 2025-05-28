"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        dummy = Node(0)

        cpy = dummy
        curr = head
        while curr:
            cpy.next = Node(curr.val)
            cpy = cpy.next
            hashmap[curr] = cpy
            curr = curr.next
        
        cpy = dummy
        curr = head
        while curr:
            if curr.random:
                cpy.next.random = hashmap[curr.random]
            cpy = cpy.next
            curr = curr.next
        
        return dummy.next