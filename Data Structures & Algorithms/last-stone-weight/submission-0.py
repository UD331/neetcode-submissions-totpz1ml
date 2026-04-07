class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-st for st in stones]
        heapq.heapify(s)
        while (len(s) > 1):
            a = heapq.heappop(s) * -1
            b = heapq.heappop(s) * -1
            if (a>b):
                heapq.heappush(s, (a-b)*-1)
        if len(s)== 1:
            return s[0]*-1
        return 0