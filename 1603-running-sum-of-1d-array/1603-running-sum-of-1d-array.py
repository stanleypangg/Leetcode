class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        ret = []
        
        for n in nums:
            sum += n
            ret.append(sum)
        
        return ret