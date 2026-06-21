class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # find all synonyms
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            elif parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_a = find(x)
            root_b = find(y)

            if root_a == root_b:
                return
            
            parent[root_a] = root_b
        
        for x, y in synonyms:
            union(x, y)
        
        groups = defaultdict(list)
        for word in parent:
            groups[find(word)].append(word)

        # make them sorted
        for key in groups:
            groups[key].sort()

        # backtracking
        text_words = text.split()
        res = []

        cur = []
        def bt(i):
            if i >= len(text_words):
                res.append(' '.join(cur))
                return
            
            word = text_words[i]
            if word in parent:
                for option in groups[find(word)]:
                    cur.append(option)
                    bt(i + 1)
                    cur.pop()
            else:
                cur.append(word)
                bt(i + 1)
                cur.pop()
        
        bt(0)
        return res