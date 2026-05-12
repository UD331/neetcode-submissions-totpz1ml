import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic ={}
        for i in nums:
            dic[i] = dic.get(i, 0)+1
        heap = []
        for key, v in dic.items():
            heapq.heappush(heap, (-v,key))
        freq = []
        for _ in range(k):
            v, key = heapq.heappop(heap)
            freq.append(key)
        return freq
            