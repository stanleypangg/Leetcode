class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        q = deque()
        q.append((beginWord, 1))
        visited = {beginWord}

        while q:
            cur, length = q.popleft()
            if cur == endWord:
                return length

            for i in range(len(cur)):
                pre, post = cur[:i], cur[i+1:]
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = pre + char + post
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        q.append((next_word, length + 1))
            
        return 0