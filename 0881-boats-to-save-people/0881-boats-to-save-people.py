class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # each boat carries max weight of limit, and at most two ppl at once
        # people[i] is the weight of the ith person
        # return min number of boats to carry every given person

        res = 0
        people.sort()

        l, r = 0, len(people) - 1
        while l <= r:
            capacity = limit - people[r]
            if l != r and people[l] <= capacity:
                l += 1
            r -= 1
            res += 1
        
        return res