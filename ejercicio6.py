class Empleados:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleados.lista_empleados.append(self)
    @classmethod
    def cantidad_empleados(cls):
     return len(cls.lista_empleados)

Empleados.lista_empleados = []

cantidad = int(input("ingrese la cantidad de empleados: "))

for _ in range(cantidad):
    nombre = input("Ingrese el nombre del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    Empleados(nombre, salario)
    


print("Cantidad de empleados:", Empleados.cantidad_empleados())
