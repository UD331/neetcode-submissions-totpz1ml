class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        fresh = 0
        time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh+=1
        while fresh and q:
            n = len(q)
            for i in range(n):
                i, j = q.popleft()
                for dr, dc in directions:
                    r = i+dr
                    c = j+dc
                    if r in range(0, rows) and c in range(0, cols) and grid[r][c] == 1:
                        grid[r][c] =2
                        fresh-=1
                        q.append((r,c))
            time+=1
        return time if fresh == 0 else -1
