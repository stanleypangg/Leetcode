class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        adj = defaultdict(list)
        for a, b in synonyms:
            adj[a].append(b)
            adj[b].append(a)
        
        word_to_group = {}
        visited = set()
        for word in adj:
            if word in visited:
                continue
            
            group = []
            q = deque([word])
            while q:
                cur = q.popleft()
                if cur in visited:
                    continue
                
                visited.add(cur)
                group.append(cur)
                
                for nei in adj[cur]:
                    q.append(nei)
            
            group.sort()
            for word in group:
                word_to_group[word] = group
        
        text_words = text.split()
        res = []

        def dfs(i, path):
            if i >= len(text_words):
                res.append(' '.join(path))
                return

            cur = text_words[i]
            if cur in word_to_group:
                for syn in word_to_group[cur]:
                    path.append(syn)
                    dfs(i + 1, path)
                    path.pop()
            else:
                path.append(cur)
                dfs(i + 1, path)
                path.pop()
        
        dfs(0, [])
        return res