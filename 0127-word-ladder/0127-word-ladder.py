class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q = deque()
        q.append(beginWord)
        visited = set()
        depth = 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return depth
                visited.add(curr)
                for i, c in enumerate(curr):
                    prefix, suffix = curr[:i], curr[i+1:]
                    for offset in range(26):
                        if ord('a') + offset == ord(c):
                            continue
                        word = prefix + chr(ord('a') + offset) + suffix
                        if word in wordList and word not in visited:
                            q.append(word)
            depth += 1
        return 0
