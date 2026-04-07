class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int row = size(grid);
        int col = size(grid[0]);
        if (row == 0 || col == 0 )
            return 0;
        int area = 0;
        for (int r = 0; r <row; r++) {
            for (int c = 0; c <col; c++) {
                if (grid[r][c] == 1) {
                    area = max(area,dfs(r,c,row,col,grid));
                }
            }
        }
        return area;
    }
    int dfs(int r, int c, int row, int col, vector<vector<int>>& grid) {
        if (r < 0 || r >= row || c < 0 || c >= col || grid[r][c] == 0)
            return 0;
        int a = 1;
        grid[r][c] = 0;
        a+= dfs(r+1,c,row,col,grid);
        a+= dfs(r-1,c,row,col,grid);
        a+= dfs(r,c+1,row,col,grid);
        a+= dfs(r,c-1,row,col,grid);
        return a;
    }
};
