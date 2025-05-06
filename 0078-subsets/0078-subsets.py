class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time and space: O(n * 2^n)
        res = []

        def bt(i, curr):
            if i > len(nums):
                return

            res.append(curr.copy())
            for j in range(i, len(nums)):
                bt(j+1, curr + [nums[j]])
        
        bt(0, [])
        return res
