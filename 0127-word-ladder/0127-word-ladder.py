class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        q = deque()
        q.append((beginWord, 1)) # store length within queue to remove depth counter

        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                pre, post = word[:i], word[i+1:]
                for c in 'abcdefghijklmnopqrstuvwxyz': # alternative to iterating 26 and using ord/chr
                    next_word = pre + c + post
                    if next_word in wordList:
                        wordList.remove(next_word) # this removes need for visited list
                        q.append((next_word, length+1))
        return 0
