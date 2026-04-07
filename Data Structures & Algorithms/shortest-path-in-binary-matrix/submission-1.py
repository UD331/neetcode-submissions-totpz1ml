class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if (grid[0][0] == 1 or grid[n-1][n-1] == 1):
            return -1
        dri = [[0,1],[1,0],[0,-1],[-1,0],
              [-1,-1], [1,1], [-1,1], [1,-1]]
        q = deque([(0, 0, 1)])
        visited = set((0,0))
        while q:
            r, c, l = q.popleft()
            if (r == n-1 and c == n-1):
                return l
            for dr, dc in dri:
                nr, nc = r + dr, c + dc
                if (nr >=0 and nr<n and nc >= 0 and nc <n and (nr, nc) not in visited and grid[nr][nc] != 1):
                    visited.add((nr, nc))
                    q.append((nr, nc, l+1))
        return -1