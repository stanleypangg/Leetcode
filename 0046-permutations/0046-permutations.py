class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(curr, remaining):
            if not remaining:
                self.res.append(curr.copy())
                return
            
            for i, n in enumerate(remaining):
                curr.append(n)
                dfs(curr, remaining[:i] + remaining[i+1:])
                curr.pop()
        
        dfs([], nums)
        return self.res