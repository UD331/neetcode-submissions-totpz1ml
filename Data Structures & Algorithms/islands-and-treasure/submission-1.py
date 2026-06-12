class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        directions = [[-1,0], [1,0], [0,-1], [0, 1]]
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                count = grid[row][col]
                for dr, dc in directions:
                    r, c = row+dr,col+dc
                    if r >= 0 and r < len(grid) and c >= 0 and c< len(grid[0]) and grid[r][c] == inf:
                        grid[r][c] = 1+count
                        q.append((r,c))
        
