import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            dic[n]=dic.get(n,0)+1
        heap = []
        for ke,v in dic.items():
            heapq.heappush(heap, (-v, ke))
        res = []
        for _ in range(k):
            v, key = heapq.heappop(heap)
            res.append(key)
        return res

            