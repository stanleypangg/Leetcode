class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.map = defaultdict(set)

        for word in dictionary:
            self.map[self._abbreviation(word)].add(word)

        print(self.map)

    def _abbreviation(self, word: str):
        if len(word) <= 2:
            return word
        else:
            between = str(len(word) - 2)
            return word[0] + between + word[-1]

    def isUnique(self, word: str) -> bool:
        cur = self._abbreviation(word)

        # no word in dictionary with same abbr OR the only word w/ same abbr is itself
        return (cur not in self.map) or (len(self.map[cur]) == 1 and word in self.map[cur])

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)