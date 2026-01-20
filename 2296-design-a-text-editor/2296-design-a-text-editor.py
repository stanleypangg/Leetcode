class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.cursor = self.tail
        self.head.next, self.tail.prev = self.tail, self.head

    def insert(self, val):
        node = Node(val, self.cursor.prev, self.cursor)
        self.cursor.prev.next = node
        self.cursor.prev = node
    
    def delete(self):
        if self.cursor.prev is self.head:
            return False
        to_delete = self.cursor.prev
        to_delete.prev.next = self.cursor
        self.cursor.prev = to_delete.prev
        return True
    
    def move_cursor(self, direction):
        if direction == 'L' and self.cursor.prev is not self.head:
            self.cursor = self.cursor.prev
            return True
        elif direction == 'R' and self.cursor.next:
            self.cursor = self.cursor.next
            return True
        return False
    
    def fetch_left(self):
        res = []
        curr = self.cursor
        i = 0
        while curr.prev is not self.head and i < 10:
            i += 1
            curr = curr.prev
            res.append(curr.val)

        return ''.join(list(reversed(res)))


class TextEditor:

    def __init__(self):
        self.list = LinkedList()

    def addText(self, text: str) -> None:
        for char in text:
            self.list.insert(char)

    def deleteText(self, k: int) -> int:
        deleted = 0
        for _ in range(k):
            if not self.list.delete():
                break
            deleted += 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        for _ in range(k):
            if not self.list.move_cursor('L'):
                break
        return self.list.fetch_left()

    def cursorRight(self, k: int) -> str:
        for _ in range(k):
            if not self.list.move_cursor('R'):
                break
        return self.list.fetch_left()


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)