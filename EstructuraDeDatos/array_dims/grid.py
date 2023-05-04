from arrays import Array

class Grid():
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_hight(self):
        return len(self.data)
    
    def get_widht(self):
        return len(self.data[0])

    def get_item(self, row, col=None):
        return self.data[row] if col==None else self.data[row][col]
    
    def set_item(self, row, col, data):
        self.data[row][col] = data

    def __str__(self) -> str:
        result = ""
        for row in range(self.get_hight()):
            for col in range(self.get_widht()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return str(result)

# grid = Grid(2,3)
# print(grid.get_hight())
# print(grid.get_widht())
# print(grid.__str__())

# for row in range(grid.get_hight()):
#     for col in range(grid.get_widht()):
#         grid.set_item(row, col, row**2+col**2)


# print(grid.__str__())
# print(grid.get_item(0))