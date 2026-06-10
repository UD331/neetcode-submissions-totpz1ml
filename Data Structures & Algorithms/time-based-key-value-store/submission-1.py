class TimeMap:
    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((-timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        heap = self.dic[key].copy()
        heapq.heapify(heap)
        while heap:
            time, val = heapq.heappop(heap)
            time*=-1
            if time <= timestamp:
                return val
        return ""
        
            
                

        
