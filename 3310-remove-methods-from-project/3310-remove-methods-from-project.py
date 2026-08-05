class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # suspicious: path starting at node k
        # if any non-suspicious points to a node in suspicious path, return original list
        # else return nodes that arent in the suspicious path

        adj = defaultdict(list)
        for u, v in invocations:
            adj[u].append(v)
        
        suspicious = set()
        def build_suspicious(node):
            if node in suspicious:
                return
            suspicious.add(node)
            for nei in adj[node]:
                build_suspicious(nei)
        build_suspicious(k)

        visited = set()
        def invokes_suspicious(node):
            if node in suspicious:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if invokes_suspicious(nei):
                    return True
                
            return False

        for i in range(n):
            if i not in suspicious and invokes_suspicious(i):
                return list(range(n))
        
        return [i for i in range(n) if i not in suspicious]