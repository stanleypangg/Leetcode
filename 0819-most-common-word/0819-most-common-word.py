class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = re.split(r"\W+", paragraph)

        most_common = None
        freq = defaultdict(int)
        for word in words:
            word = word.lower()
            if word in banned:
                continue

            freq[word] += 1
            if freq[most_common] < freq[word]:
                most_common = word

        return most_common.lower()