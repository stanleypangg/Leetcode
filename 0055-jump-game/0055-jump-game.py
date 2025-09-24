class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # just need to make it past all 0s
        jump = 0
        for pos, num in enumerate(nums):
            jump = max(jump, pos + num)
            if jump >= len(nums) - 1:
                return True
            elif jump == pos:
                return False
        