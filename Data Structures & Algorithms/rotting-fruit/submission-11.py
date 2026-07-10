class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        fresh = 0
        time = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh:
            time+=1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        fresh-=1
                        grid[r][c] = 2
                        q.append((r,c))

        return time if fresh == 0 else -1
