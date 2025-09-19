class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # approach: turn wordlist into a graph and find shortest path
        # shortest path can just be done by bfs
        # how to transform wordList into a graph? every neighbour differs by one letter
        # adj list? undirected
        
        # O(n^2) building adj list: represent each word as a counter
        # iterate wordList, check other words if counter differs by one -> O(w)
        # trie? actual comparsion check would be O(w)
        
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        wordList.add(beginWord)
        wordList = list(wordList)

        # adj = {word: neighbours}
        adj = defaultdict(set)
        
        # building adj : O(n^2 * w)
        for i in range(len(wordList)):
            a = wordList[i]
            for j in range(i + 1, len(wordList)):
                diff = 0
                b = wordList[j]
                for k in range(len(a)):
                    if a[k] != b[k]:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    adj[a].add(b)
                    adj[b].add(a)
        
        # shortest path search
        # O(n * w)
        q = deque()
        q.append(beginWord)
        visited = set()
        depth = 1
        while q:
            length = len(q)
            for _ in range(length):
                curr = q.popleft()
                visited.add(curr)
                if curr == endWord:
                    return depth
                for neighbour in adj[curr]:
                    if neighbour not in visited:
                        q.append(neighbour)
            depth += 1
        return 0