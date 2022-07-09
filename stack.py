class Stack:
    def __init__(self):
        self.stack = list()

    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True

        else:
            return False

    def peek(self):
        return self.stack[-1]

t = Stack()
t.add(9)
t.add(6)
print(t.peek())

        
        

        
        