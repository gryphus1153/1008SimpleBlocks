from Stack import Stack
from RoboFunctions import Robot

# Load the block world configuration to the tables


def load(filename, initial, table, final):
    f = open(filename, "r")
    state = "initial"
    for line in f:
        line = line.strip()
        if line[0] == "#":
            state = "initial"
        elif line[0] == "$":
            state = "final"
        elif line[0] == "|":
            stack = Stack()
            line = line[1:].split(",")
            for block in line:
                if block != "":
                    stack.push(block)

            if state == "initial":
                initial.append(stack)
                tableStack = stack.copyTo()
                table.append(tableStack)
            else:
                final.append(stack)

# Achieve final state by solving left to right


def leftPlanner(table, final):
    for toStack in range(len(final)):
        for height, goalBlock in enumerate(final[toStack].data):
            print("Goal: " + goalBlock + " to " + str(toStack))
            fromStack = findBlockinTable(table, goalBlock)
            tempStack = findTempStack(table, toStack, fromStack)
            if fromStack != toStack:
                clearStack(table, toStack, tempStack, height)
                stackMoveBlock(table, toStack, fromStack, tempStack, goalBlock)
            else:
                if table[toStack].peekAt(height) == goalBlock:
                    print(goalBlock + " is already in correct position")
                else:
                    goalTemp = findTempStack(table, tempStack, fromStack)
                    stackMoveBlock(table, goalTemp, fromStack,
                                   tempStack, goalBlock)
                    clearStack(table, toStack, tempStack, height)
                    robot.move(table, goalTemp, toStack)


def clearStack(table, toStack, tempStack, height):
    for i in range(height, table[toStack].size()):
        robot.move(table, toStack, tempStack)


def findTempStack(table, toStack, fromStack):
    for stackNo in range(len(table)):
        if stackNo != toStack and stackNo != fromStack:
            return stackNo


def findBlockinTable(table, block):
    for stackNo in range(len(table)):
        if block in table[stackNo].data:
            return stackNo


def stackMoveBlock(table, toStack, fromStack, tempStack, goalBlock):
    for block in table[fromStack].data[::-1]:
        if block != goalBlock:
            robot.move(table, fromStack, tempStack)
        else:
            robot.move(table, fromStack, toStack)
            break


# contains N amount of stacks
initial = []
final = []
table = []
robot = Robot()

# initialization
load("Tables/test.txt", initial, table, final)
leftPlanner(table, final)
print(robot.moveCount)
