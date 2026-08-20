class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products = set(products)

        for i, c in enumerate(searchWord):
            products = {p for p in products if i < len(p) and p[i] == c}
            print(products)

            heap = []
            for p in products:
                if len(heap) < 3:
                    heapq.heappush_max(heap, p)
                else:
                    heapq.heappushpop_max(heap, p)
            
            heap.sort()
            res.append(heap)

        return res