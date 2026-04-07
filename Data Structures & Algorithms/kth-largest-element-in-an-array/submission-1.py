class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = [-n for n in nums]
        heapq.heapify(s)
        while k > 1:
            k-=1
            heapq.heappop(s)
        return heapq.heappop(s)*-1