class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        st = []

        for i, num in enumerate(nums):
            while st and st[-1] > num and len(st) + n - i > k:
                st.pop()
            
            if len(st) < k:
                st.append(num)
        
        return st