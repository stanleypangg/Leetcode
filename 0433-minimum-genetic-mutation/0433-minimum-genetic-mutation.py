class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        mutations = 0
        start_visited = {startGene}
        start_queue = deque([startGene])
        end_visited = {endGene}
        end_queue = deque([endGene])

        while start_queue and end_queue:
            if len(start_queue) > len(end_queue):
                start_queue, end_queue = end_queue, start_queue
                start_visited, end_visited = end_visited, start_visited
            
            cur = start_queue.popleft()
            for i in range(8):
                for c in 'ACGT':
                    new_gene = cur[:i] + c + cur[i+1:]
                    if new_gene in end_visited:
                        return mutations + 1
                    
                    if new_gene in bank and new_gene not in start_visited:
                        start_visited.add(new_gene)
                        start_queue.append(new_gene)
            
            mutations += 1
        
        return -1