class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        chars = [(count, char) for char, count in freq.items()]
        chars.sort(key=lambda x: -x[0])
        return ''.join([char * count for char, count in chars])