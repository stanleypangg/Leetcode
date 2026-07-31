# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        st = []
        num = ''
        last = None

        for c in s:
            if c.isdigit() or c == '-':
                num += c
            elif c == ',' and num:
                st[-1].add(NestedInteger(int(num)))
                num = ''
            elif c == '[':
                new_list = NestedInteger()
                if st:
                    st[-1].add(new_list)
                st.append(new_list)
            elif c == ']':
                if num:
                    st[-1].add(NestedInteger(int(num)))
                    num = ''
                last = st.pop()
        
        return last if last else NestedInteger(int(num))