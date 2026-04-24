class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        mh = [-cnt for cnt in count.values()]
        heapq.heapify(mh)
        t = 0
        q = deque()
        while mh or q:
            t+=1
            if not mh:
                t = q[0][1]
            else:
                cnt = 1 + heapq.heappop(mh)
                if cnt:
                    q.append([cnt,t+n])
            if q and q[0][1] == t:
                heapq.heappush(mh,q.popleft()[0])
        return t
    
        