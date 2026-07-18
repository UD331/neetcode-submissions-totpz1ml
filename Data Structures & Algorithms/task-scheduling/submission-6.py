class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        q = deque()
        t = 0

        while q or heap:
            t+=1
            if not heap:
                t = q[0][1]
            else:
                cnt = 1+heapq.heappop(heap)
                if cnt:
                    q.append([cnt, t+n])
            if q and q[0][1] == t:
                heapq.heappush(heap, q.popleft()[0])

        return t
                