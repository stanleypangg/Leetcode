class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        for i in range(len(temperatures)):
            while st and temperatures[i] > st[-1][0]:
                index = st.pop()[1]
                res[index] = i - index
            st.append((temperatures[i], i))
        
        return res