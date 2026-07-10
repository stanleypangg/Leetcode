class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        component = [0] * n

        for i in range(1, n):
            component[i] = component[i - 1] + (abs(nums[i] - nums[i - 1]) > maxDiff)

        return [component[i] == component[j] for i, j in queries]