class Array:
    def __init__(self, capacity, fill_Value=None):
        self.items = list()

        for _ in range(capacity): 
            self.items.append(fill_Value)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self) -> str:
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

# menu = Array(5)
# for i in range(0,5):
#     menu.__setitem__(i, i**2)

# print(menu.__len__())
# menu.__setitem__(1,3)
# print(menu.__str__())

# print(menu.__getitem__(3))

