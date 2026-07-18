import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        heap = [(-v,key) for key, v in dic.items()]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            v, key = heapq.heappop(heap)
            res.append(key)
        return res

            