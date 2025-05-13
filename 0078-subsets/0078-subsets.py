class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        def dfs(i, curr):
            if i >= len(nums):
                self.res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            dfs(i + 1, curr)
        
        dfs(0, [])
        return self.res