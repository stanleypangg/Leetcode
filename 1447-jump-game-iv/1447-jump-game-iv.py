class Solution:
    def minJumps(self, arr: List[int]) -> int:
        visited = [False] * len(arr)
        visited[0] = True
        indices = defaultdict(list)

        for i, n in enumerate(arr):
            indices[n].append(i)
        
        depth = 0
        q = deque([0])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == len(arr) - 1:
                    return depth

                if cur - 1 >= 0 and not visited[cur - 1]:
                    q.append(cur - 1)
                    visited[cur - 1] = True

                if cur + 1 < len(arr) and not visited[cur + 1]:
                    q.append(cur + 1)
                    visited[cur + 1] = True
                
                for idx in indices[arr[cur]]:
                    if idx == cur:
                        continue
                    
                    if not visited[idx]:
                        q.append(idx)
                        visited[idx] = True
                
                del indices[arr[cur]]
        
            depth += 1