class Solution {
private:
    int m;
    int n;

    void dfs(int r, int c, vector<vector<char>>& grid) {
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == '0') return;
        grid[r][c] = '0';
        dfs(r + 1, c, grid);
        dfs(r - 1, c, grid);
        dfs(r, c + 1, grid);
        dfs(r, c - 1, grid); 
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;

        m = grid.size();
        n = grid[0].size();

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == '1') {
                    res++;
                    dfs(r, c, grid);
                }
            }
        }

        return res;
    }
};