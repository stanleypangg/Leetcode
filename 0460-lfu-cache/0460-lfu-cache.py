class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self):
        # no need for capacity
        self.head = Node(-1, 0)
        self.tail = Node(-1, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0
    
    def _add_node(self, node):
        tail = self.tail
        prev = self.tail.prev

        prev.next = node
        node.prev, node.next = prev, tail
        tail.prev = node

        self.size += 1
    
    def _remove_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        
        self.size -= 1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} # key -> [node, count]
        self.freq_lru = {} # freq -> LRUCache
        self.min_freq = 0 # min freq used

        # challange -> determine min efficiently (doubly linked list in sorted order?)
        # challenge -> LRU tie breaker (LRU cache for every freq?)

        # challenge -> how to keep track of LFU in O(1)? linked list bruh

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # update count, move to next freq LRUCache
            node, freq = self.hashmap[key]

            # remove this node from its LRU
            old_freq_lru = self.freq_lru[freq]
            old_freq_lru._remove_node(node)
            if old_freq_lru.size == 0:
                del self.freq_lru[freq]
                if self.min_freq == freq:
                    self.min_freq += 1 # now that there are no nodes with freq == self.min_freq

            self.hashmap[key][1] += 1 # increase freq
            _, freq = self.hashmap[key] # get updated freq

            if freq not in self.freq_lru: # if new LRU doesn't exist
                self.freq_lru[freq] = LRUCache()

            lru_cache = self.freq_lru[freq] # add to LRU
            lru_cache._add_node(node)

            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        # If key already exists
        if self.get(key) != -1: # self.get handles it all!
            node, _ = self.hashmap[key]
            node.val = value # all we need to do is update value
            return
        
        # If capacity full
        if self.capacity == len(self.hashmap):
            # Evict
            lru_cache = self.freq_lru[self.min_freq]
            lru = lru_cache.head.next # we have to make sure its empty
            lru_cache._remove_node(lru)
            del self.hashmap[lru.key]
            if lru_cache.size == 0:
                del self.freq_lru[self.min_freq]
        
        if 1 not in self.freq_lru: # if new LRU doesn't exist
            self.freq_lru[1] = LRUCache()
        
        lru_1 = self.freq_lru[1]
        new_node = Node(key, value)
        lru_1._add_node(new_node)
        self.hashmap[key] = [new_node, 1]

        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)