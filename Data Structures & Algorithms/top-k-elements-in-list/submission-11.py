import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic ={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        heap = []
        for num, freq in dic.items():
            heap.append((-freq, num))
        
        heapq.heapify(heap)
        
        result = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)
        
        return result