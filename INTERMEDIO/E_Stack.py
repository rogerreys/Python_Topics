from A_node import Node

class Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            
            if self.top.next:
                self.top = self.top.next
            else: 
                self.top = None

            return data
        else:
            return "void"
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return 'void'
    
    def clear(self):
        while self.top:
            self.pop()

    def search(self, data):
        probe = self.top
        while probe:
            if probe.data == data:
                return probe
            probe = probe.next
        return 'void'
            
    
    def getDatas(self):
        probe = self.top
        data = ""
        while probe:
            data += probe.data+" "
            probe = probe.next
        return data.strip()
