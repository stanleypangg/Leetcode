class Solution:
    def bestClosingTime(self, customers: str) -> int:
        res = max_score = score = 0
        for i in range(1, len(customers) + 1):
            score += 1 if customers[i - 1] == 'Y' else -1
            if score > max_score:
                max_score = score
                res = i
        return res