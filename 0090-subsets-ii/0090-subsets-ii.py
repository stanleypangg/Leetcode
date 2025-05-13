class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []

        def dfs(curr, start):
            self.res.append(curr.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                dfs(curr, i + 1)
                curr.pop()
        
        dfs([], 0)
        return self.res