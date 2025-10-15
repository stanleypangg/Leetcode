class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 4 circular wheels
        # slots 0-9
        # wheels rotate freely and can wrap around
        # initial node = '0000'

        # deadends indicate lack of edge
        # return minimum = bfs

        # how to reduce visited?
        # if we store every single combination -> 10 ** 4
        
        # we only ever need to go towards the target

        deadends = set(deadends)
        if '0000' in deadends:
            return -1

        q = deque(['0000'])
        visited = set()
        visited.add('0000')
        depth = 0
        while q:
            length = len(q)
            for _ in range(length):
                curr = q.popleft()
                if curr == target:
                    return depth

                for i in range(4):
                    prefix, suffix = curr[:i], curr[i + 1:]
                    curr_wheel = int(curr[i])

                    forward = prefix + str((curr_wheel + 1) % 10) + suffix
                    if forward not in visited and forward not in deadends:
                        q.append(forward)
                        visited.add(forward)

                    backward = prefix + str((curr_wheel -1) % 10) + suffix
                    if backward not in visited and backward not in deadends:
                        q.append(backward)
                        visited.add(backward)
                
            depth += 1

        return -1
