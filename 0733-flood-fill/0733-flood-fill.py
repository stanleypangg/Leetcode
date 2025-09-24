class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image
            
        m, n = len(image), len(image[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(r, c):
            image[r][c] = color
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == orig:
                    dfs(nr, nc)

        dfs(sr, sc)

        return image
            