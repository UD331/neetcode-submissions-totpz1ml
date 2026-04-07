class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            z = x - y
            if z < 0 :
                heapq.heappush(heap, z)
        if not heap: return 0
        return -(heapq.heappop(heap))