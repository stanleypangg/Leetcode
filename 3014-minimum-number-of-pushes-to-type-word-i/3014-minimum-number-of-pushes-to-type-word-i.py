class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sort = sorted((cnt for cnt in freq.values()), reverse=True)

        res = mapped = 0
        for cnt in sort:
            res += cnt * (mapped // 8 + 1)
            mapped += 1

        return res