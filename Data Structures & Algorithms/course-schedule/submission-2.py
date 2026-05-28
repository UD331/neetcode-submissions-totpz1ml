class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crs = defaultdict(list)
        for a, b in prerequisites:
            crs[a].append(b)

        visited = set()

        def dfs(n):
            if n in visited:
                return False
            if crs[n] == []:
                return True
            visited.add(n)
            for pre in crs[n]:
                if not dfs(pre):
                    return False
            crs[n] = []
            visited.remove(n)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False

        return True