class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        res = [0] * 5
        blocks = defaultdict(int)

        for r, c in coordinates:
            if r < m - 1 and c < n - 1:
                blocks[(r, c)] += 1

            if r > 0 and c < n - 1:
                blocks[(r - 1, c)] += 1

            if r < m - 1 and c > 0:
                blocks[(r, c - 1)] += 1

            if r > 0 and c > 0:
                blocks[(r - 1, c - 1)] += 1

        for black in blocks.values():
            res[black] += 1
        
        res[0] = (m - 1) * (n - 1) - len(blocks)
        return res