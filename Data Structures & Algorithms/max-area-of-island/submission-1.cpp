class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int row = size(grid);
        int col = size(grid[0]);
        if (row == 0 || col == 0 )
            return 0;
        int area = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    area = max(dfs(i, j, row, col, grid), area);
                }
            }
        }
        return area;
    }
    int dfs(int r, int c, int row, int col, vector<vector<int>>& grid) {
        if (r >= row || c >= col || r <0 || c < 0 || grid[r][c] == 0) {
            return 0;
        }
        grid[r][c] = 0;
        int area = 1; 
        area += dfs(r + 1, c, row, col, grid);
        area += dfs(r - 1, c,row, col,  grid);
        area += dfs(r, c + 1,row, col,  grid);
        area += dfs(r, c - 1,row, col,  grid);
        return area;
    }
};
