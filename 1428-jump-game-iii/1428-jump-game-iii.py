class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        q = deque([start])

        while q:
            idx = q.popleft()
            
            if arr[idx] == 0:
                return True
            
            visited.add(idx)
            
            forward = idx + arr[idx]
            if forward < len(arr) and forward not in visited:
                q.append(forward)
            
            backward = idx - arr[idx]
            if backward >= 0 and backward not in visited:
                q.append(backward)
            
        return False