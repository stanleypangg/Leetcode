class Node:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.hashmap = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next, self.tail.prev = self.tail, self.head
        
        for n in nums:
            self.add(n)
    
    def showFirstUnique(self) -> int:
        if self.head.next is self.tail:
            return -1
        return self.head.next.val

    def add(self, value: int) -> None:
        if value in self.hashmap:
            node = self.hashmap[value]
            if node:
                node.prev.next, node.next.prev = node.next, node.prev
                self.hashmap[value] = None
        else:
            node = Node(value, self.tail.prev, self.tail)
            self.tail.prev.next = self.tail.prev = node
            self.hashmap[value] = node

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)