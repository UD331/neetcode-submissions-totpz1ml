class MinStack:
    def __init__(self):
        self.st = []
        self.m = []

    def push(self, val: int) -> None:
        self.st.append(val)
        val = min(val, self.m[-1] if self.m else val)
        self.m.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.m.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.m[-1]
