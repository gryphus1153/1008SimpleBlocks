class Stack:
    def __init__(self):
        self.data = []
        self.bottom = 0

    def size(self):
        return len(self.data)

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if not self.isEmpty():
            return self.data[self.size() - 1]

    def peekAt(self, pos):
        return self.data[pos]

    def copyTo(self):
        stack = Stack()
        for ele in self.data:
            stack.push(ele)
        return stack