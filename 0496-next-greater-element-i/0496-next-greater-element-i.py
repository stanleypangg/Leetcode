class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        st = []

        for num in nums2:
            while st and num > st[-1]:
                top = st.pop()
                ans[top] = num
            st.append(num)
        
        return [ans.get(num, -1) for num in nums1]