class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in wordList:
            return 0

        begin_set = {beginWord}
        end_set = {endWord}
        visited = set()
        steps = 1

        while begin_set and end_set:
            # balance exploring on both ends
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_set = set()
            for word in begin_set:
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        if char == word[i]:
                            continue
                        
                        next_word = word[:i] + char + word[i+1:]
                        if next_word in end_set:
                            return steps + 1
                        
                        if next_word in word_set and next_word not in visited:
                            next_set.add(next_word)
                            visited.add(next_word)
                
            begin_set = next_set
            steps += 1
        
        return 0
