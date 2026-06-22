class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # croak
        # freq[c] >= freq[r] >= freq[o] >= freq[a] >= freq[k]

        # croakcrook
        # c: 2
        # r: 2
        # o: 3
        # a: 1
        # k: 1

        res = 0
        prev = {
            'c': '',
            'r': 'c',
            'o': 'r',
            'a': 'o',
            'k': 'a'
        }
        freq = defaultdict(int)
        freq[''] = float('inf')

        for char in croakOfFrogs:
            freq[char] += 1
            if freq[char] > freq[prev[char]]:
                return -1

            if char == 'k':
                for char in 'croak':
                    freq[char] -= 1

            num_frogs = max(freq[char] for char in 'croak')
            res = max(res, num_frogs)

        for char in 'roak':
            if freq[char] != freq['c']:
                return -1

        return res