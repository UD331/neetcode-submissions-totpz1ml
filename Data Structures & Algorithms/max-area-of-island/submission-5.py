class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            if r not in range(row) or c not in range(col) or grid[r][c] ==0:
                return 0
            grid[r][c] = 0
            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c-1)+dfs(r,c+1)

        m = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    m = max(m,dfs(r,c))
        return m