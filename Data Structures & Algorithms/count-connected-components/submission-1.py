class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False]*n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(i):
            for j in adj[i]:
                if not visited[j]:
                    visited[j] = True
                    dfs(j)

        c = 0

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                c+=1

        return c
