class Aprendiz:
    def __init__(self, nombres, apellidos, cedula, sexo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.sexo = sexo
        self.formacion = input("Programa de formacion: ")
        self.regional = input("Regional: ")
        
    def mostrar_info(self):
        print("Hola, soy un aprendiz SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Sexo: {self.sexo}")
        print(f"Estudiante del programa: {self.formacion}")
        print("--------------------------------------------------------")
        
class Instructor:
    def __init__(self, nombres, apellidos, cedula, area):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.area = area
    
    def mostrar_info(self):
        print("Hola, soy un instructor SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Area de instruccion: {self.area}")
        print("--------------------------------------------------------")

class Coordinador:
    def __init__(self, nombres, apellidos, cedula, departamento):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.departamento = departamento
    
    def mostrar_info(self):
        print("Hola, soy un coordinador del SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Departamento: {self.departamento}")
        print("--------------------------------------------------------")

def mostrar_informacion(persona):
    persona.mostrar_info()
    
objeto_aprendiz = Aprendiz("Juan","Hernandez Silva", 12334556789, "Masculino")
objeto_instructor = Instructor("Laura","Rodriguez", 987644211, "Programacion")
objeto_coordinador = Coordinador("Carlos","Perez", 8927446294, "Recursos Humanos")

mostrar_informacion(objeto_aprendiz)
mostrar_informacion(objeto_instructor)
mostrar_informacion(objeto_coordinador)
