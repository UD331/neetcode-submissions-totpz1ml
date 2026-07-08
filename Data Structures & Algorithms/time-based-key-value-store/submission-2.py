class TimeMap:
    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.dic[key], (-timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        heap = self.dic[key].copy()
        while heap:
            time, val = heapq.heappop(heap)
            if time*-1 <= timestamp:
                return val
        return ""
            
                

        
