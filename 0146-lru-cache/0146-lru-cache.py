class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru
    
    def remove_node(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def add_node(self, node):
        prev, next = self.mru.prev, self.mru
        prev.next = next.prev = node
        node.prev = prev
        node.next = next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.add_node(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add_node(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self.remove_node(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)