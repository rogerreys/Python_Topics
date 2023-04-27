from grid import Grid
from arrays import Array

class Cube():
    def __init__(self, rows, cols, depts, fill_value= None) -> None:
        self.data = Grid(rows, cols)

        for row in range(self.data.get_hight()):
            for col in range(self.data.get_widht()):
                self.data.set_item(row, col, Array(depts, fill_value)) 
    
    def get_depth(self):
        return len(self.data.get_item(0,0))
    
    def get_hight(self):
        return self.data.get_hight()
    
    def get_widht(self):
        return self.data.get_widht()
    
    def get_dimension(self):
        return self.get_widht(), self.get_hight(), self.get_depth()
    
    def __str__(self) -> str:
        return self.data.__str__()
    
    def set_data(self, row, col, dep, data):
        self.data.get_item(row, col)[dep] = data

    def set_get(self, row, col, dep):
        return self.data.get_item(row, col)[dep]
    
cube = Cube(3,3,3)
print(cube.__str__())

for row in range(cube.get_hight()):
    for col in range(cube.get_widht()):
        for dep in range(cube.get_depth()):
            cube.set_data(row, col, dep, row**2+col**2+dep**2)


print(cube.__str__())