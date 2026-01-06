class FileSystem:

    def __init__(self):
        # valid format is (/\w+)+
        self.trie = {}

    def createPath(self, path: str, value: int) -> bool:
        parts = path.split('/')[1:]
        if not parts:
            return False

        curr = self.trie
        for part in parts[:-1]:
            if part not in curr:
                return False
            curr, _ = curr[part]

        last = parts[-1]
        if last in curr:
            return False
        
        curr[last] = ({}, value)
        return True

    def get(self, path: str) -> int:
        parts = path.split('/')[1:]
        if not parts:
            return -1

        curr = self.trie
        for part in parts[:-1]:
            if part not in curr:
                return -1
            curr = curr[part][0]
        
        last = parts[-1]
        return -1 if last not in curr else curr[last][1]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)