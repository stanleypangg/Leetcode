class Solution:
    def rob(self, nums: List[int]) -> int:
        # Yes you can leave some in between
        one = two = 0

        for n in nums:
            subproblem = max(one, n + two)
            one, two = subproblem, one
        
        return one
