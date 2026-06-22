class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        return min(min(freq[c] for c in 'ban'), min(freq[c] // 2 for c in 'lo'))