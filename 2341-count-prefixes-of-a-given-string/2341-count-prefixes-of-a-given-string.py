class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        # array words, string
        # all lowercase english
        # return # of strings in words that are a prefix of s
        # iterate over each word, checking each prefix
        res = 0

        def checkPrefix(prefix, word):
            if len(prefix) > len(word):
                return False

            for i in range(len(prefix)):
                if prefix[i] != word[i]:
                    return False
            return True

        for word in words:
            if checkPrefix(word, s):
                res += 1
        return res