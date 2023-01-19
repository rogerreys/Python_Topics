from rectangulo import Rectangulo

# Clase hija
class Cuadrado(Rectangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)
        