class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_set = set(nums)
        length = len(num_set)
        if 0 in num_set:
            length -= 1
        return length