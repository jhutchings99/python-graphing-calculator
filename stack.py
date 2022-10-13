class Stack:
    def __init__(self):
        self.mData = []

    def push(self, item):
        self.mData.append(item)

    def top(self):
        return self.mData[-1]

    def pop(self):
        return self.mData.pop()

    def isEmpty(self):
        return len(self.mData) == 0