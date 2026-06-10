class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crs = defaultdict(list)
        for c, pre in prerequisites:
            crs[c].append(pre)
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
            visited.remove(c)
            crs[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True