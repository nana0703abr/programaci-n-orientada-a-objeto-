class estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas if isinstance(notas, list) else []

    def agregar_nota(self, nota):
        if nota < 0 or nota > 100:
            raise ValueError("la nota debe estar entre 0 y 100")
        self.notas.append(nota)

    def calcular_promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def obtener_informacion(self):
        return f"nombre: {self.nombre}, edad: {self.edad}, notas: {self.notas}"
    
nombre = input("ingrese el nombre del estudiante: ")
edad = int(input("ingrese la edad del estudiante: "))
notas = [float(nota) for nota in input("ingrese las notas del estudiante separadas por comas: ").split(",")]
estudiante1 = estudiante(nombre, edad, notas)
print(estudiante1.obtener_informacion())
print("promedio de notas:", estudiante1.calcular_promedio())
nueva_nota = float(input("ingrese una nueva nota para el estudiante: "))
estudiante1.agregar_nota(nueva_nota)
print("promedio actualizado de notas:", estudiante1.calcular_promedio())
