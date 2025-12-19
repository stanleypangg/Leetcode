class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # encoding: #<int><word>
        # int describes length of word
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        print(res)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = curr_len = 0
        while i < len(s):
            while s[i] != '#':
                curr_len = curr_len * 10 + int(s[i])
                i += 1
            res.append(s[i + 1: i + 1 + curr_len])
            i += 1 + curr_len
            curr_len = 0

        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))