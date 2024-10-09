class Carro:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def descripcion(self):
        print(f"Soy un {self.tipo}. Tengo cuatro ruedas y un motor.")
        print("-------------------------------------------------------------")

class Moto:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def descripcion(self):
        print(f"Soy una {self.tipo}. Tengo dos ruedas y un motor.")
        print("-------------------------------------------------------------")
        
class Bicicleta:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def descripcion(self):
        print(f"Soy una {self.tipo}. Tengo dos ruedas y no tengo motor.")
        print("-------------------------------------------------------------")
        
def mostrar_informacion(vehiculo):
    vehiculo.descripcion()

mi_carro = Carro("Carro Toyota modelo 2015")
mi_moto = Moto("Moto Kawasaki modelo 2018")
mi_bici = Bicicleta("Bicicleta BMX")

mostrar_informacion(mi_carro)
mostrar_informacion(mi_moto)
mostrar_informacion(mi_bici)
