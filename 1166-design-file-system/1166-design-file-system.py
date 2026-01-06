class FileSystem:

    def __init__(self):
        # valid format is (/\w+)+
        self.trie = {}

    def createPath(self, path: str, value: int) -> bool:
        directories = path.split('/')[1:]

        curr = self.trie
        for i in range(len(directories) - 1):
            directory = directories[i]
            if directory not in curr:
                return False
            curr = curr[directory][0]
        
        if directories[-1] in curr:
            return False
        
        curr[directories[-1]] = [{}, value]
        return True

    def get(self, path: str) -> int:
        directories = path.split('/')[1:]
        curr = self.trie

        for i in range(len(directories) - 1):
            directory = directories[i]
            if directory not in curr:
                return -1
            curr = curr[directory][0]
        
        last = directories[-1]
        return -1 if last not in curr else curr[last][1]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)