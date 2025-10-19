class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # complement = target - curr
        hashmap = {} # number -> index in nums
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hashmap:
                return [i, hashmap[comp]]
            hashmap[num] = i
        