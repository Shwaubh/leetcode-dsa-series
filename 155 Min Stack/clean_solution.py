class MinStack:

    def __init__(self):
        self.stack = []
        self.getmin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.getmin:
            lastmin = self.getmin[-1]
            self.getmin.append(min(lastmin, val))
        else:
            self.getmin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.getmin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.getmin[-1]

