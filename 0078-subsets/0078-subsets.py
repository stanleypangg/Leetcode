class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time and space: O(n * 2^n)
        res = []

        subset = []
        def bt(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            bt(i + 1)
            subset.pop()
            bt(i + 1)
        
        bt(0)
        return res
