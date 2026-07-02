class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        tallest = 0

        for i in range(len(heights) -1, -1, -1):
            h = heights[i]
            if h > tallest:
                res.append(i)
                tallest = h
        
        res.reverse()
        return res