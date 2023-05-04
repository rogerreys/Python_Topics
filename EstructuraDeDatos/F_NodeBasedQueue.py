
class TwoWayNode(object):
    def __init__(self, data=None, next=None, previous=None) -> None:
        self.data = data
        self.next = next
        self.previous = previous

class Queue():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0
    
    def enqueue(self, data):
        newQueue = TwoWayNode(data)
        if self.tail == None:
            self.head = newQueue
            self.tail = self.head
        else:
            newQueue.previous = self.tail
            self.tail.next = newQueue
            self.tail = newQueue
        self.count += 1

    def dequeue(self):
        current = self.head
        if self.count == 1:
            self.head = None
            self.tail = None
        else: 
            self.head = current.next 
            self.head.previous = None
        self.count -= 1

        return current.data