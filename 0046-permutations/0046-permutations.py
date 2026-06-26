class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(cur, remaining):
            if not remaining:
                res.append(cur.copy())
                return
            
            for n in remaining:
                bt(cur + [n], remaining - {n})
        
        num_set = set(nums)
        for n in nums:
            bt([n], num_set - {n})
        
        return res