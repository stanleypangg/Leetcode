class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = defaultdict(int)

        for i in range(minSize, maxSize + 1):
            window = {}

            l = 0
            for r, c in enumerate(s):
                length = r - l + 1
                window[c] = window.get(c, 0) + 1

                if length < i:
                    continue
                elif length > i:
                    window[s[l]] -= 1                    
                    if window[s[l]] == 0:
                        del window[s[l]]

                    l += 1

                if len(window) > maxLetters:
                    continue
            
                string = s[l: r + 1]
                freq[string] += 1

        if not freq:
            return 0
            
        return max(v for v in freq.values())