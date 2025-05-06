class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(i, curr, total):
            if total == target:
                # valid combo found
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                # bad combo, backtrack
                return
            
            bt(i, curr + [candidates[i]], total + candidates[i])
            bt(i + 1, curr, total)
        
        bt(0, [], 0)
        return res
