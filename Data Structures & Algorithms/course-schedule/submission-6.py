class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for p, c in prerequisites:
            pre[p].append(c)
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if pre[crs] == []:
                return True
            visit.add(crs)
            for p in pre[crs]:
                if not dfs(p):
                    return False
            visit.remove(crs)
            pre[crs] = []
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
        