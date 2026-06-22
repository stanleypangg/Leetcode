class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        brightness = defaultdict(int)
        min_val = float('inf')
        max_val = float('-inf')

        for p, r in lights:
            left, right = p - r, p + r
            min_val = min(min_val, left)
            max_val = max(max_val, right)

            brightness[left] += 1
            brightness[right + 1] -= 1
    
        res = None
        max_brightness = running = 0
        for i in sorted(brightness.keys()):
            running += brightness[i]
            if max_brightness < running:
                res = i
                max_brightness = running
        
        return res