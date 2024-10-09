class Guitarra:
    def __init__(self, tipo):
        self.tipo = tipo

    def descripcion(self):
        print(f"Soy una guitarra {self.tipo}. Se utilizan seis cuerdas para producir sonidos.")
        print("-----------------------------------------------")

class Piano:
    def __init__(self, tamaño):
        self.tamaño = tamaño

    def descripcion(self):
        print(f"Soy un piano de {self.tamaño}. Tengo 88 teclas y produzco una amplia gama de sonidos.")
        print("-----------------------------------------------")

class Trompeta:
    def __init__(self, material):
        self.material = material

    def descripcion(self):
        print(f"Soy una trompeta de {self.material}. Soy un instrumento de viento metal.")
        print("-----------------------------------------------")
        
def mostrar_informacion(instrumentos):
    instrumentos.descripcion()

guitarra = Guitarra("Acustica")
piano = Piano("Clasico")
trompeta = Trompeta("Oro")

mostrar_informacion(guitarra)
mostrar_informacion(piano)
mostrar_informacion(trompeta)