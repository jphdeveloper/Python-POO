class Perro:
    def __init__(self, raza):
        self.raza = raza

    def descripcion(self):
        print(f"Soy un {self.raza}. Soy leal y juguetón.")
        print("-----------------------------------------------")

class Gato:
    def __init__(self, color):
        self.color = color

    def descripcion(self):
        print(f"Soy un gato {self.color}. Soy independiente y curioso.")
        print("-----------------------------------------------")

class Pajaro:
    def __init__(self, color):
        self.color = color

    def descripcion(self):
        print(f"Soy un pájaro {self.color}. Puedo volar y canto melodías.")
        print("-----------------------------------------------")
        
def mostrar_informacion(animal):
    animal.descripcion()

perro = Perro("Golden Retriever")
gato = Gato("Naranja")
pajaro = Pajaro("Australiano")

mostrar_informacion(perro)
mostrar_informacion(gato)
mostrar_informacion(pajaro)