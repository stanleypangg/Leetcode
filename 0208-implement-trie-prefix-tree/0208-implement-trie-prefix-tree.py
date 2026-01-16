class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = [{}, False]
            prev = curr
            curr, _ = curr[c]
        prev[c][1] = True # mark end of word

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            prev = curr
            curr, _ = curr[c]
        return prev[c][1] # mark end of word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr, _ = curr[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)