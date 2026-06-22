class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        for i, size in enumerate(groupSizes):
            group = groups[size]
            if not group or len(group[-1]) == size:
                group.append([i])
            else:
                group[-1].append(i)

        res = []
        for group in groups.values():
            res.extend(group)
        return res