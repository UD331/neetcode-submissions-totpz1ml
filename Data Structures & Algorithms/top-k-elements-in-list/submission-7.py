import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for n in nums:
            c[n] = 1+c.get(n, 0)
        heap = []
        for key in c.keys():
            heapq.heappush(heap,(c[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res