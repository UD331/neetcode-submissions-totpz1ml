class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        // this is just practice for bfs source code
        int row = grid.size(),  col = grid[0].size();
        vector<pair<int, int>> dir = {{-1,0}, {1, 0}, {0,-1}, {0, 1}};
        queue<pair<int, int>> q;
        int f = 0;
        for(int r = 0; r <row; r++)
            for(int c = 0; c<col; c++)
                if (grid[r][c] == 1)
                    f++;
                else if (grid[r][c] == 2)
                    q.push({r,c});
        int t = 0;
        while (q.size() != 0 && f != 0) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                int r = q.front().first, c = q.front().second;
                q.pop();
                for (pair<int,int> d:dir) {
                    int r1 = r+d.first, c1 = c+d.second;
                    if (r1 >= 0 && r1 < row && c1 >=0 && c1 <col) {
                        if (grid[r1][c1] == 1) {
                            q.push({r1,c1});
                            grid[r1][c1] = 2;
                            f--;
                        }
                    }
                }
            }
            t++;
        }
        if (f > 0)
            return -1;
        return t;
    }
};
