class Queue:
    def __init__(self):
        self.queue = list()

    def add(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True

        else:
            return False

    def remove(self):
        self.queue.pop()

t = Queue()
t.add(9)
t.add(6)
t.remove()
print(t.queue)
        
        

        
        