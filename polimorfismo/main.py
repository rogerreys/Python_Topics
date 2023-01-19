from ciclista import Ciclista
from persona import Persona

def run():
    persona = Persona("Pepe")
    ciclista = Ciclista("Luis")
    persona.avanza()
    ciclista.avanza()

if __name__ == '__main__':
    run()