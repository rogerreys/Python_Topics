from persona import Persona

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print("Ando moviendome en mi bicicleta")
