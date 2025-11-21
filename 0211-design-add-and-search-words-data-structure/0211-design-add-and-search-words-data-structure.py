# Use a Trie for the word search
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.end_of_word
            
            nextt = word[i]

            if nextt == '.':
                return any(dfs(node.children[child], i + 1) for child in node.children)
            elif nextt in node.children:
                return dfs(node.children[nextt], i + 1)
            
            return False
        
        return dfs(self.trie, 0)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)