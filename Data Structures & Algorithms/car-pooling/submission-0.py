class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        minHeap = []
        curPass = 0
        for np, f, t in trips:
            while minHeap and minHeap[0][0]<=f:
                curPass-=heapq.heappop(minHeap)[1]
            curPass+=np
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, (t,np))

        return True
