class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        res = None
        max_postfix = float('-inf')
        postfix = 0
        
        for i in range(len(gas) - 1, -1, -1):
            postfix += gas[i] - cost[i]
            if postfix > max_postfix:
                max_postfix = postfix
                res = i
        
        return res