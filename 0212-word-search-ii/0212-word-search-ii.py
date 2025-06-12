class TrieNode:
    def __init__(self, word):
        self.children = {}
        self.word = word

class Trie:
    def __init__(self):
        self.root = TrieNode(False)
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(False)
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        m, n = len(board), len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)

        dirs = {(0, 1), (0, -1), (1, 0), (-1, 0)}
        
        def bt(curr, node, r, c, visited):
            visited.add((r, c))
            
            if node.word:
                res.append(curr)
                node.word = False
            
            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                if (0 <= new_r < m and 0 <= new_c < n and 
                    board[new_r][new_c] in node.children and
                    (new_r, new_c) not in visited):
                    ch = board[new_r][new_c]
                    bt(curr + ch, node.children[ch], new_r, new_c, visited)

            visited.remove((r, c))
        
        for r in range(m):
            for c in range(n):
                ch = board[r][c]
                if ch in trie.root.children:
                    bt(ch, trie.root.children[ch], r, c, set())
        
        return res