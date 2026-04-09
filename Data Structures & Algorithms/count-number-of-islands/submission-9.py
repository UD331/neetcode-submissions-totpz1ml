class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r not in range(0, ROWS) or c not in range(0, COLS) or grid[r][c] =="0":
                return
            grid[r][c]='0'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands+=1
                    dfs(r,c)
        return islands

