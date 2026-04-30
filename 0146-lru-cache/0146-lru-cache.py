class Node:
    def __init__(self, key = 0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _evict(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _append(self, node):
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev.next = self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self._evict(node)
        self._append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self._evict(node)
            self._append(node)
            return
    
        if self.capacity == 0:
            to_evict = self.head.next
            del self.hashmap[to_evict.key]
            self._evict(to_evict)
            self.capacity += 1
    
        node = Node(key, value)
        self.hashmap[key] = node
        self._append(node)
        self.capacity -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)