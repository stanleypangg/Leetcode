class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = [] # monotonic decreasing stack, i.e. keep the min at the top

        for i in range(len(temperatures) - 1, -1, -1):
            while st and st[-1][0] <= temperatures[i]:
                st.pop()
            
            if st:
                res[i] = st[-1][1] - i

            st.append((temperatures[i], i))
        
        return res
        