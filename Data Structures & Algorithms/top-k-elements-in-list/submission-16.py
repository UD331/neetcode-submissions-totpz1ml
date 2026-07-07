import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        heap = []
        for key,v in dic.items():
            heapq.heappush(heap, [-v,key])
        res = []
        print(heap)
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        

            