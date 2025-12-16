class Solution:
    def countAndSay(self, n: int) -> str:
        def rle_encode(string: str) -> str:
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

        if n == 1:
            return '1'

        rle = '1'
        for _ in range(n - 1):
            rle = rle_encode(rle)
        
        return rle