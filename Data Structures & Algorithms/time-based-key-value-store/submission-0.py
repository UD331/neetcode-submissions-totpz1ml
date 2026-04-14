class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((timestamp, value))
        else:
            self.dic[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        vals = self.dic[key]
        l, r = 0, len(vals)-1
        c = -1
        while l <= r:
            m = (l+r)//2
            t, v = vals[m]
            if t > timestamp:
                r = m-1
            elif t == timestamp:
                return v
            else:
                if c == -1:
                    c = m
                else:
                    tc, vc = vals[c]
                    if t > tc:
                        c = m
                l = m+1
        if c == -1:
            return ""
        t, v = vals[c]
        return v
            
                

        
