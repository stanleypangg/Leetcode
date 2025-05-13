class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []

        def dfs(total, start, curr):
            if total > target:
                return
            elif total == target:
                self.res.append(curr.copy())
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                curr.append(candidates[i])
                dfs(total + candidates[i], i + 1, curr)
                curr.pop()
        
        dfs(0, 0, [])
        return self.res