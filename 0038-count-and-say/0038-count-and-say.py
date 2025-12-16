class Solution:
    def rle_encode(self, string: str) -> str:
        encoding = []

        i = 0
        while i < len(string):
            j = i + 1
            while j < len(string) and string[j] == string[j - 1]:
                j += 1
            encoding.append(str(j - i))
            encoding.append(string[i])
            i = j
        
        return ''.join(encoding)

    def countAndSay(self, n: int) -> str:
        rle = '1'

        for _ in range(n - 1):
            rle = self.rle_encode(rle)
        
        return rle