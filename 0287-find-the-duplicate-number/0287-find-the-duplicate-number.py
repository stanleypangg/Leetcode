class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) time, O(1) space
        # Floyd cycle detection to find beginning of cycle
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow