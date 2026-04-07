class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visited, prev):
            if r not in range(0, rows) or c not in range(0, cols) or (r,c) in visited or heights[r][c] < prev:
                return
            visited.add((r,c))
            dfs(r-1,c,visited, heights[r][c])
            dfs(r+1,c,visited, heights[r][c])
            dfs(r,c-1,visited, heights[r][c])
            dfs(r,c+1,visited, heights[r][c])

        atl, pac = set(), set()
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append((r,c))
        return res