class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        st = []

        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                index, height = st.pop()
                res = max(res, (i - index) * height)
                start = index
            st.append((start, h))
        
        for i, h in st:
            res = max(res, (len(heights) - i) * h)
        
        return res