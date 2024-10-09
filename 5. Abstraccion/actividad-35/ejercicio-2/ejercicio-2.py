from abc import ABC, abstractmethod
import math

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_base):
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

class EmpleadoPorHoras(Empleado):
    def __init__(self, tarifa_por_hora, horas_trabajadas):
        self.tarifa_por_hora = tarifa_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.tarifa_por_hora * self.horas_trabajadas

empleado_tiempo_completo = EmpleadoTiempoCompleto(3000)
print(f"Salario del empleado a tiempo completo: {empleado_tiempo_completo.calcular_salario()}")
empleado_por_horas = EmpleadoPorHoras(15, 160)
print(f"Salario del empleado por horas: {empleado_por_horas.calcular_salario()}")