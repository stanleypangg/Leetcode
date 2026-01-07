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
            
            # determine length of strings
            remaining = maxWidth - length
            if num_words == 1:
                res.append(pack[0] + ' ' * remaining)
            elif i == n - 1:
                word = ' '.join(pack)
                word += ' ' * (maxWidth - len(word))
                res.append(word)
            else:
                # pad in between each string
                word = [pack[0]]
                num_gaps = num_words - 1
                extra = remaining % num_gaps
                spaces = remaining // num_gaps
                for j in range(extra):
                    word.append(' ' * (spaces + 1))
                    word.append(pack[j + 1])
                for j in range(extra, num_gaps):
                    word.append(' ' * spaces)
                    word.append(pack[j + 1])
                res.append(''.join(word))
            i += 1
        return res