class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # initial power of power, score of 0
        # tokens[i] = value of token_i
        # maximize total score by strategically playing these tokens
        # in a move, play an unplayed token
        # face-up: power is at least tokens[i] -> lose tokens[i] power and gain 1 score
        # face-down: score is at least 1 -> gain tokens[i] and lose 1 score

        if not tokens:
            return 0

        tokens.sort()
        if power < tokens[0]:
            return 0

        res = score = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                res = max(res, score)
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        
        return res