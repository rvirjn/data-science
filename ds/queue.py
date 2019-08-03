"""
Queue data Structure
D
C
B
A
"""

class Queue():
    def __init__(self):
        self.items = []

    def enqueued(self, item):
        self.items.append(item)

    def dequeued(self):
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


s = Queue()
print(s.get_stack())