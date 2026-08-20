class TrieNode:
    def __init__(self, end_of_sentence=False):
        self.children = {}
        self.end_of_sentence = end_of_sentence

class AutocompleteSystem:

    def _insert(self, s, t=1):
        self.freq[s] += t
        cur = self.trie
        for c in s:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_sentence = True

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = TrieNode()
        self.cur = self.trie
        self.freq = defaultdict(int)
        self.history = []

        for s, t in zip(sentences, times):
            self._insert(s, t)

    def input(self, c: str) -> List[str]:
        if c == '#':
            self._insert(''.join(self.history))
            self.cur = self.trie
            self.history = []
            return []

        self.history.append(c)
        if c not in self.cur.children:
            self.cur = TrieNode() # invalidate every further input
            return []
        self.cur = self.cur.children[c]

        heap = []
        def dfs(cur, path):
            if cur.end_of_sentence:
                sentence = ''.join(path)
                if len(heap) < 3:
                    heapq.heappush_max(heap, (-self.freq[sentence], sentence))
                else:
                    heapq.heappushpop_max(heap, (-self.freq[sentence], sentence))
            for c in cur.children:
                dfs(cur.children[c], path + [c])
        
        dfs(self.cur, [''.join(self.history)])
        heap.sort()
        return [s for _, s in heap]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)