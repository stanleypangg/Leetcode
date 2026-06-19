class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        m = len(similarPairs)
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            elif parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for x, y in similarPairs:
            union(x, y)

        return all(find(x) == find(y) for x, y in zip(sentence1, sentence2))