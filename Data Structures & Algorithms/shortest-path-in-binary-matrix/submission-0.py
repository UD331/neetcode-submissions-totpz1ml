class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if (grid[0][0] == 1 or grid[n-1][n-1] == 1):
            return -1
        dri = [[0,1],[1,0],[0,-1],[-1,0],
              [-1,-1], [1,1], [-1,1], [1,-1]]
        q = deque([(0, 0, 1)])
        visit = set((0, 0))
        while q:
            r, c, l = q.popleft()
            if r == n-1 and c == n-1:
                return l
            for dr, dl in dri:
                nr = r+dr
                nl = c+dl
                if (nr >= 0 and nr <n and 
                    nl >= 0 and nl <n and
                    (nr, nl) not in visit and 
                    grid[nr][nl] == 0):
                    q.append((nr,nl,l+1))
                    visit.add((nr,nl))
        return -1