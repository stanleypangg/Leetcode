class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = [0] * (2 * len(nums))
        
        for i in range(len(nums)):
            lst[i] = nums[i]
            lst[i+len(nums)] = nums[i]
        
        return lst