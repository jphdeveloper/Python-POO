from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

class Ingeniero(TareaEmpleado):
    def realizar_tarea(self):
        print("Estoy diseñando un nuevo sistema.")

class Doctor(TareaEmpleado):
    def realizar_tarea(self):
        print("Estoy atendiendo a un paciente.")

ingeniero = Ingeniero()
doctor = Doctor()

ingeniero.realizar_tarea()
doctor.realizar_tarea()