class FileSystem:

    def __init__(self):
        self.file = {} # path -> (file name, content)
        self.trie = {}
    
    def _traverse(self, path):
        if path == '/':
            return self.trie

        cur = self.trie
        for part in path.split('/')[1:]:
            if part not in cur:
                cur[part] = {}
            cur = cur[part]
        return cur

    def ls(self, path: str) -> List[str]:
        if path in self.file:
            return [self.file[path][0]]
        node = self._traverse(path)
        return list(sorted(node.keys()))

    def mkdir(self, path: str) -> None:
        self._traverse(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath in self.file:
            self.file[filePath][1] += content
            return
        
        directory, file_name = filePath.rsplit('/', 1)
        node = self._traverse(directory)
        node[file_name] = file_name
        self.file[filePath] = [file_name, content]

    def readContentFromFile(self, filePath: str) -> str:
        return self.file[filePath][1]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)