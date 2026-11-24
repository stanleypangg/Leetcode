class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        t1_larger = []
        t2_larger = []

        for i, (t1, t2) in enumerate(zip(technique1, technique2)):
            if t1 >= t2:
                t1_larger.append(i)
            else:
                t2_larger.append(i)
        
        k -= len(t1_larger)
        need = max(0, k)

        t2_larger.sort(key=lambda i: (technique2[i] - technique1[i]))

        return (
            sum(technique1[i] for i in t1_larger) + 
            sum(technique1[i] for i in t2_larger[:need]) + 
            sum(technique2[i] for i in t2_larger[need:])
        )