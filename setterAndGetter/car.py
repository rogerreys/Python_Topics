class Car:
    __color = str
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color