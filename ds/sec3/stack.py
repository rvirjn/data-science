"""
Stack data Structure
D
C
B
A
"""


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items

    def top(self):
        return self.items[-1]

    def get_size(self):
        return len(self.items)


s = Stack()
s.push('A')
s.push('B')
s.pop()
s.push('C')
print(s.get_size())
s.push('D')
print(s.get_stack())