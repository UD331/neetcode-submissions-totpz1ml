class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crs = defaultdict(list)
        for cr, p in prerequisites:
            crs[cr].append(p)
        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if crs[c] == []:
                return True
            visited.add(c)
            for pre in crs[c]:
                if not dfs(pre):
                    return False
            crs[c] = []
            visited.remove(c)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True