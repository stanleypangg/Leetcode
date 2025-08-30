class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.size = 0
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, index: int) -> int:
        # Iteration: O(n)
        if index >= self.size:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        first = self.head.next
        new_node = Node(val, self.head, first)

        self.head.next = new_node
        first.prev = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        last = self.tail.prev
        new_node = Node(val, last, self.tail)

        self.tail.prev = new_node
        last.next = new_node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        if index == self.size:
            self.addAtTail(val)
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        nxt = prev.next
        
        new_node = Node(val, prev, nxt)
        prev.next = new_node
        nxt.prev = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        to_del = prev.next
        nxt = to_del.next

        prev.next = nxt
        nxt.prev = prev

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)