class Solution:

    def __init__(self):
        self.st = []
        self.mini = None

    def push(self, x):
        if not self.st:
            self.mini = x
            self.st.append(x)
        else:
            if x >= self.mini:
                self.st.append(x)
            else:
                self.st.append(2 * x - self.mini)
                self.mini = x

    def pop(self):
        if not self.st:
            return -1
        
        top = self.st.pop()
        if top < self.mini:
            self.mini = 2 * self.mini - top

    def peek(self):
        if not self.st:
            return -1
        top = self.st[-1]
        if top >= self.mini:
            return top
        else:
            return self.mini

    def getMin(self):
        if not self.st:
            return -1
        return self.mini