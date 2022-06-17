from collections import deque


from collections import deque

class stacks:
    def __init__(self):
        self.jaggi=deque()

    def push(self,value):
        self.jaggi.append(value)

    def peek(self):
        return self.jaggi[-1]


shah = stacks()
str="We will conquere COVID-19"

for i in str:
    shah.push(i)

for i in reversed(shah.jaggi):
    print(i,end="")
