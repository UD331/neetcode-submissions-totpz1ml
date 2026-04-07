class MinStack:
    stack = []
    mi = 0
    mi_stack = []
    def __init__(self):
        self.stack = []
        self.mi_stack = []
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.mi_stack.append(val)
            self.stack.append(val)
        else:
                self.stack.append(val)
                val = min(val, self.mi_stack[-1])
                self.mi_stack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.mi_stack.pop(-1)


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mi_stack[-1]

