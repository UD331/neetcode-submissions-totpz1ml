class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        for crs, p in prerequisites:
            pre[crs].append(p)

        visit, cycle = set(), set()
        res = []

        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            for p in pre[node]:
                if not dfs(p):
                    return False
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        return res