class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        if len(currentState) < 2:
            return []
        
        res = []
        for i in range(len(currentState) - 1):
            if currentState[i] == currentState[i + 1] == '+':
                res.append(currentState[:i] + '--' + currentState[i + 2:])
        
        return res