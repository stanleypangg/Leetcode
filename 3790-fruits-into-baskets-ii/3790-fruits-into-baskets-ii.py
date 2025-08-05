class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # n types of fruits and n baskets
        # fruits[i] = quantity of ith fruit
        # baskets[j] = size of jth basket
        # rules:
        # ith fruit type must be in leftmost basket with capacity >= fruits[i]
        # basket can only have one fruit tyype
        # if fruit cannot ber placed -> unplaced
        # return # of fruit types that can be placed

        # brute force: O(n^2)
        # for each fruit, find first sufficient basket
        res = len(fruits)
        for f in fruits:
            for i, b in enumerate(baskets):
                if f <= b:
                    res -= 1
                    baskets[i] = 0
                    break
        return res