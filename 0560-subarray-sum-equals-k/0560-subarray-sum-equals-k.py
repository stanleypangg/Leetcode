class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = {0: 1}

        running_sum = 0
        for n in nums:
            running_sum += n
            complement = running_sum - k

            if complement in prefix:
                res += prefix[complement]
            
            prefix[running_sum] = prefix.get(running_sum, 0) + 1
        
        return res