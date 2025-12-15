class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort()

        st = []
        for i in range(len(pairs) - 1, -1, -1):
            p, s = pairs[i]
            time = (target - p) / float(s)

            if st and time <= st[-1]:
                continue
            
            st.append(time)
        
        return len(st)