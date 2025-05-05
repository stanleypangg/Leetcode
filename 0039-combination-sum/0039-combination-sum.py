class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def bt(combination):
            curr = sum(combination)
            combination.sort()
            if curr == target and combination not in res:
                res.append(combination)
            elif curr > target:
                return
            else:
                i = 0
                while i < len(candidates) and candidates[i] + curr <= target:
                    bt(combination + [candidates[i]])
                    i += 1
        
        bt([])
        return res