class ValidWordAbbr:

    def _abbr(self, word: str) -> str:
        mid = '' if len(word) <= 2 else str(len(word) - 2)
        return word[0] + mid + word[-1]

    def __init__(self, dictionary: List[str]):
        # word in dictionary and freq[abbr(word)] == 1
        # freq[abbr(word)] == 0

        self.dictionary = set(dictionary)
        self.freq = defaultdict(int)

        for word in self.dictionary:
            self.freq[self._abbr(word)] += 1

    def isUnique(self, word: str) -> bool:
        abbr = self._abbr(word)
        return (word in self.dictionary and self.freq[abbr] == 1) or (self.freq[abbr] == 0)

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)