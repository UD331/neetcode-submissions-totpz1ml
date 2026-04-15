class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.capacity = capacity
        self.st = []

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        self.st.remove(key)
        self.st.append(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.st.remove(key)
            self.st.append(key)
        else:
            if len(self.st) >= self.capacity:
                k = self.st[0]
                self.st.pop(0)
                self.dic.pop(k)   
            self.st.append(key)
        self.dic[key] = value
        
        

