class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        q = deque()
        t = 0

        while heap or q:
            t+=1
            if not heap:
                t = q[0][0]
            else:
                c = 1+heapq.heappop(heap)
                if c:
                    q.append([t+n,c])
            if q and q[0][0] == t:
                heapq.heappush(heap, q.popleft()[1])
        return t
                