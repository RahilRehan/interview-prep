# O(1) t.c, O(n) s.c in worst case
class Stack:
    def __init__(self):
        self.s = []
        self.m = []

    def empty(self) -> bool:
        return len(self.s) == 0

    def max(self) -> int:
        if not self.empty():
            return self.m[-1][0]
        else:
            raise IndexError("max on empty stack")

    def pop(self) -> int:
        if not self.empty():
            if self.s[-1] == self.m[-1][0]:
                if self.m[-1][1] == 1:
                    self.m.pop()
                else:
                    self.m[-1] = (self.m[-1][0], self.m[-1][1]-1)
            return self.s.pop()
        else:
            raise IndexError("pop on empty stack") 

    def push(self, x: int) -> None:
        if not self.empty():
            if x > self.m[-1][0]:
                self.m.append((x, 1))
            elif x == self.m[-1][0]:
                self.m[-1] = (self.m[-1][0], self.m[-1][1]+1)
            self.s.append(x)
        else:
            self.s.append(x)
            self.m.append((x, 1))

# optimized, O(1) t.c and O(1) space
class Stack:
    def __init__(self):
        self.stack = []
        self.maxi = float("-inf")
    
    def empty(self) -> bool:
        return len(self.stack) == 0
    
    def max(self) -> int:
        return self.maxi
    
    def push(self, x: int):
        if self.empty():
            self.maxi = x
            self.stack.append(x)
        else:
            if x <= self.maxi:
                self.stack.append(x)
            else:
                self.stack.append(2*x-self.maxi)
                self.maxi = x

    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop on empty stack")
        top = self.stack[-1]
        if top > self.maxi:
            real = self.maxi
            self.maxi = 2*real - top
            self.stack.pop()
            return real
        return self.stack.pop()