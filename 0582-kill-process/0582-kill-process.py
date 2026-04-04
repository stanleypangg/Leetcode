class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        adj = defaultdict(list)
        for idx, idd in enumerate(ppid):
            adj[idd].append(pid[idx])

        res = []

        q = deque([kill])
        while q:
            cur = q.popleft()
            res.append(cur)
            if cur in adj:
                q.extend(adj[cur])

        return res