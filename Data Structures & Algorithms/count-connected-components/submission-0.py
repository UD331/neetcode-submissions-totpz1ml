class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(no):
            for ne in adj[no]:
                if not visit[ne]:
                    visit[ne] = True
                    dfs(ne)

        res = 0
        for no in range(n):
            if not visit[no]:
                visit[no] = True
                dfs(no)
                res+=1
        return res