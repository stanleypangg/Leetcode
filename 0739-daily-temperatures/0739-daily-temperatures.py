class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        for i, t in enumerate(temperatures):
            while st and t > st[-1][0]:
                index = st.pop()[1]
                res[index] = i - index
            st.append((t, i))
        
        return res