class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        matchsticks.sort(reverse=True)
        target = total // 4
        visited = set()

        def bt(one, two, three, four, i):
            key = tuple(sorted([one, two, three, four]))
            if key in visited:
                return False

            visited.add(key)
            
            if one > target or two > target or three > target or four > target:
                return False

            if i == len(matchsticks):
                if one == two == three == four:
                    return True
                return False
            
            cur = matchsticks[i]
            i += 1

            return (
                bt(one + cur, two, three, four, i) or \
                bt(one, two + cur, three, four, i) or \
                bt(one, two, three + cur, four, i) or \
                bt(one, two, three, four + cur, i)
            )
        
        return bt(0, 0, 0, 0, 0)