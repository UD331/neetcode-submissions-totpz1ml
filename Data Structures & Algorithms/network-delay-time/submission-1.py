class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for ui, vi, ti in times:
            adj[ui].append((vi,ti))
        dist = {node: float('inf') for node in range(1,n+1)}

        def dfs(u,t):
            if t >= dist[u]:
                return

            dist[u] = t
            for ui, vi in adj[u]:
                dfs(ui, t+vi)

        dfs(k, 0)

        res = max(dist.values())
        return -1 if res == float('inf') else res