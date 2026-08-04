class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        res = []

        for i in range(cols):
            r, c = 0, i
            while r < rows and c < cols:
                index = r * cols + c
                res.append(encodedText[index])
                r += 1
                c += 1
        
        return ''.join(res).rstrip()