class Node:
    def __init__(self, val, prev = None, next = None, cached = False):
        self.val = val
        self.prev = prev
        self.next = next
        self.cached = cached

    def remove(self):
        # Remove self from linked list
        temp = self.prev
        self.prev.next = self.next
        self.next.prev = temp
        self.cached = False
    
    def insert(self, node):
        # insert node after self
        temp = self.next
        self.next = node
        node.prev, node.next = self, temp
        temp.prev = node 
        node.cached = True

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # hashmap: key -> node
        # node has prev, next, val, isCached
        # prev and next to do removal in O(1)
        self.hashmap = {}

        # initialize dummy nodes
        self.head = Node(0) # head
        self.tail = Node(0) # tail
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        # O(1): use a hashmap
        # get: get the key, if exists, check if its within cache
        # check within cache: keep a boolean

        if key in self.hashmap and self.hashmap[key].cached:
            # Enforce LRU
            # Remove Node, and insert at tail
            node = self.hashmap[key]
            node.remove()
            self.tail.prev.insert(node)

            return node.val
        
        return -1


    def put(self, key: int, value: int) -> None:
        # O(1): use a hashmap to put
        # use a linked list to enforce LRU policy
        # evict LRU is self.capacity == 0
        
        if self.get(key) != -1:
            # Key exists, self.get handles LRU policy
            node = self.hashmap[key]
            node.val = value
            return

        # Otherwise, we insert at end, and handle it ourselves
        if self.capacity == 0:
            # Not enough space, we need to evict
            self.head.next.remove()
            self.capacity += 1
        
        new_node = Node(value)
        self.hashmap[key] = new_node # create new node
        self.tail.prev.insert(new_node)
        self.capacity -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)