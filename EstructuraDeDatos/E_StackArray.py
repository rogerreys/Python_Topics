from array_dims.arrays import Array

class StackArray(Array):
    def __init__(self, capacity, fill_Value=None):
        super().__init__(capacity, fill_Value)
        self.size = 0
        self.top = self.size
    
    def push(self, new_item):
        self.__setitem__(self.size, new_item)
        self.size += 1
        self.top = self.size-1

    def pop(self):
        data = self.__getitem__(self.top)
        self.__setitem__(self.top, None)
        self.size -=1
        self.top = self.size
        return data

    def peek(self):
        return self.__getitem__(self.top)

    def clear(self):
        while self.__getitem__(self.top):
            self.pop()

    def getData(self):
        data = ""        
        for i in range(self.size):
            data += self.__getitem__(i) + " "
        return data.strip()