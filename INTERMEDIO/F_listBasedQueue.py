class ListQueue:
    def __init__(self):
        self.item = []
        self.size = 0

    def enqueue(self, data):
        self.item.insert(0, data)
        self.size += 1
    
    def dequeue(self):
        data = self.item.pop()
        self.size -= 1
        return data
    
    def traversel(self):
        for i in self.item:
            print(i)
