import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            dic[n] = 1 + dic.get(n, 0)
        heap = []
        for ke, v in dic.items():
            heapq.heappush(heap, (-v, ke))
        l = []
        for i in range(k):
            v, ke = heapq.heappop(heap)
            l.append(ke)
        return l
