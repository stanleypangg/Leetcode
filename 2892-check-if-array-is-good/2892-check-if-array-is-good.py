class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        freq = Counter(nums)

        for i in range(1, n):
            if i not in freq or freq[i] != 1:
                return False
        
        return freq[n] == 2