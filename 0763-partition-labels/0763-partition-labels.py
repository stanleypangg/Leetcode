class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # greedy
        # get the leftmost and rightmost indices of each char
        # try to grab the smallest range, see which other chars are in there
        # and make sure their ranges fit, if not, we have to extend the range

        res = []
        last = {c : s.rindex(c) for c in set(s)}

        seen = set()
        partition = set()
        l = r = 0
        while r < len(s):
            # first seen in this partition
            if s[r] not in seen:
                seen.add(s[r])
                partition.add(s[r])
            
            # if its the last index
            if r == last[s[r]]:
                partition.remove(s[r])

            if not partition:
                res.append(r - l + 1)
                seen = set()
                partition = set()
                l = r + 1

            r += 1
        return res