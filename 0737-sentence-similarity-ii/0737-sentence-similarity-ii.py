class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        parent = {}
        size = {}

        def find(x):
            if x not in parent:
                parent[x] = x
                size[x] = 1
            elif parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return
            
            if size[root_x] < size[root_y]:
                root_x, root_y = root_y, root_x
            
            parent[root_y] = root_x
            size[root_x] += size[root_y]
        
        for x, y in similarPairs:
            union(x, y)

        return all(find(x) == find(y) for x, y in zip(sentence1, sentence2))