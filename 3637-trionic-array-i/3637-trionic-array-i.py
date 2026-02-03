class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        i = 1
        while i < n and nums[i - 1] < nums[i]:
            i += 1

        if i == 1:
            return False
        
        p = i
        while i < n and nums[i - 1] > nums[i]:
            i += 1
        
        if i == p:
            return False

        q = i
        while i < n and nums[i - 1] < nums[i]:
            i += 1

        if i == q:
            return False

        return i == n
