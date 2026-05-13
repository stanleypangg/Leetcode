class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            change = 1 if direction == 1 else -1
            diff[start] += change
            diff[end + 1] -= change

        res = []
        prefix = 0

        for i, c in enumerate(s):
            prefix += diff[i]

            old_pos = ord(c) - ord('a')
            new_pos = (old_pos + prefix) % 26

            res.append(chr(new_pos + ord('a')))
        
        return ''.join(res)