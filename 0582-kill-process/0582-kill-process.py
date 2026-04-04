class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        n = len(pid)
        adj = {idd: [] for idd in pid}
        adj[0] = []

        # idd is pid[idx]'s parent
        for idx, idd in enumerate(ppid):
            adj[idd].append(pid[idx])

        res = []

        q = deque([kill])
        while q:
            cur = q.popleft()
            res.append(cur)
            for cid in adj[cur]:
                q.append(cid)

        return res