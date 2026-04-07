class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        row, col = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        while fresh != 0 and q:
            l = len(q)
            for i in range(l):
                r,c = q.popleft()
                for dr, dc in directions:
                    ro, co = r+dr, c +dc
                    if (ro in range(len(grid))
                        and co in range(len(grid[0]))
                        and grid[ro][co] == 1
                    ):
                        grid[ro][co] = 2
                        q.append((ro, co))
                        fresh -= 1
            time+=1
        return time if fresh ==0 else -1