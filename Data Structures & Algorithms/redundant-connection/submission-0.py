class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges)+1)]

        def dfs(node, par):
            if visit[node]:
                return True
            visit[node] = True
            for n in adj[node]:
                if n == par:
                    continue
                if dfs(n, node):
                    return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] *(len(edges)+1)
            if dfs(u, -1):
                return [u,v]
        return []
