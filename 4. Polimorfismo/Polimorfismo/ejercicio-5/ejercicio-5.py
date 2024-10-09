class Medico:
    def __init__(self, especialidad):
        self.especialidad = especialidad

    def descripcion(self):
        print(f"Soy un médico especialista en {self.especialidad}. Me dedico a cuidar la salud de las personas.")
        print("-----------------------------------------------------------------------------------------")

class Ingeniero:
    def __init__(self, rama):
        self.rama = rama

    def descripcion(self):
        print(f"Soy un ingeniero en {self.rama}. Diseño y construyo soluciones tecnológicas.")
        print("-----------------------------------------------------------------------------------------")
class Docente:
    def __init__(self, materia):
        self.materia = materia

    def descripcion(self):
        print(f"Soy un docente de {self.materia}. Transmito conocimientos a mis estudiantes.")
        print("-----------------------------------------------------------------------------------------")
        
def mostrar_informacion(profesiones):
    profesiones.descripcion()

medico = Medico("Urologia")
ingeniero = Ingeniero("Sistema")
docente = Docente("Quimica")

mostrar_informacion(medico)
mostrar_informacion(ingeniero)
mostrar_informacion(docente)