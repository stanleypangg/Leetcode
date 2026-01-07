class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        res = []
        i = 0
        while i < len(words):
            pack = [words[i]]
            num_words = 1
            length = len(words[i])

            # pack more words
            while i + 1 < len(words) and len(words[i + 1]) + length + num_words <= maxWidth:
                i += 1
                pack.append(words[i])
                length += len(words[i])
                num_words += 1
            
            line = ''
            # determine length of strings
            remaining = maxWidth - length
            if num_words == 1:
                line = pack[0] + ' ' * remaining
            elif i == n - 1:
                line = ' '.join(pack)
                line += ' ' * (maxWidth - len(line))
            else:
                # pad in between each string
                line = pack[0]
                num_gaps = num_words - 1
                extra = remaining % num_gaps
                spaces = remaining // num_gaps
                for j in range(num_gaps):
                    to_add = spaces + (1 if extra > 0 else 0)
                    line += ' ' * to_add + pack[j + 1]
                    if extra:
                        extra -= 1
            res.append(line)
            i += 1
        return res