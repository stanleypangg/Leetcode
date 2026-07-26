# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.cursor = 0
        self.st = []
    
    def next(self) -> int:
        if not self.hasNext():
            # should not hit this
            return -1
            
        val, _ = self.st.pop()
        return val.getInteger()
    
    def hasNext(self) -> bool:
        while True:
            if not self.st:
                if self.cursor >= len(self.nestedList):
                    return False
            
                lst = self.nestedList[self.cursor]
                self.st.append((lst, 0))
                self.cursor += 1

            top, index = self.st[-1]
            if top.isInteger():
                return True
            
            self.st.pop()
            lst = top.getList()

            if index >= len(lst):
                continue
            
            if index + 1 < len(lst):
                self.st.append((top, index + 1))
            
            self.st.append((lst[index], 0))

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())