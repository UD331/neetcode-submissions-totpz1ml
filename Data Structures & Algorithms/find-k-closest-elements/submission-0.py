class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [[abs(i-x), i] for i in arr]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return sorted(res)