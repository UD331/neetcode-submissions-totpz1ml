class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int R = grid.size();
        int C = grid[0].size();
        if (R == 0 || C == 0)
            return 0;
        int n = 0;

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (grid[i][j] == '1') {
                    dfs(i, j, grid);
                    cout << i << "\t" << j << "\n";
                    n++;
                }
            }
        }
        return n;
    }
    
    void dfs(int r, int c,vector<vector<char>>& grid) {
        if ((r >= grid.size()) || (c == grid[0].size()) || r < 0 || c <0
        || grid[r][c] == '0')
            return;
        grid[r][c] = '0';
        dfs(r+1, c, grid);
        dfs(r-1, c, grid);
        dfs(r, c-1, grid);
        dfs(r, c+1, grid);

    }
};
