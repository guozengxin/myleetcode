#!/usr/bin/env python
# https://oj.leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minStack) == 0 or x < self.minStack[-1][0]:
            self.minStack.append((x, 1))
        elif x == self.minStack[-1][0]:
            self.minStack[-1] = (x, self.minStack[-1][1] + 1)

    # @return nothing
    def pop(self):
        if self.top() == self.getMin():
            if self.minStack[-1][1] > 1:
                self.minStack[-1] = (self.minStack[-1][0], self.minStack[-1][1] - 1)
            else:
                self.minStack.pop()
        return self.stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.minStack[-1][0]

if __name__ == '__main__':
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    stack.push(1)
    print stack.getMin()
    print stack.pop()
    print stack.getMin()
