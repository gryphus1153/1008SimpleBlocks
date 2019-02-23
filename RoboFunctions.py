class Robot:
    def __init__(self):
        self.arm = None
        self.moveCount = 0

    def isEmpty(self):
        return self.arm == None

    def unstack(self, table, stackNo):
        if self.isEmpty:
            self.arm = table[stackNo].pop()

    def stack(self, table, stackNo):
        if not self.isEmpty():
            table[stackNo].push(self.arm)
            self.arm = None

    def move(self, table, fromStack, toStack):
        if self.isEmpty:
            self.unstack(table, fromStack)
            print(self.arm + ": " + str(fromStack) + " -> " + str(toStack))
            self.stack(table, toStack)
            self.moveCount += 1
            
    def countReset(self):
        self.moveCount = 0