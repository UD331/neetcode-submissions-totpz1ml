class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(r,c,prevH,s):
            if r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prevH or (r,c) in s:
                return
            s.add((r,c))
            dfs(r-1, c, heights[r][c],s)
            dfs(r+1, c, heights[r][c],s)
            dfs(r, c-1, heights[r][c],s)
            dfs(r, c+1, heights[r][c],s)

        atl = set()
        pac = set()

        for r in range(rows):
            dfs(r, 0, heights[r][0],pac)
            dfs(r,cols-1,heights[r][cols-1],atl)

        for c in range(cols):
            dfs(0, c, heights[0][c],pac)
            dfs(rows-1,c,heights[rows-1][c],atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])

        return res