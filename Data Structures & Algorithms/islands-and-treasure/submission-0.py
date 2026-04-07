class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        directions = [[-1,0], [1,0], [0,-1], [0, 1]]
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        while q:
            for n in range(len(q)):
                i, j, k = q.popleft()
                for dr, dc in directions:
                    r = i + dr
                    c = j + dc
                    if r in range(0, rows) and c in range(0, cols) and grid[r][c] == inf:
                        grid[r][c] = k+1
                        q.append((r,c,k+1))
