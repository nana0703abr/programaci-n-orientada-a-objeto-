class libro:
    def __init__(self, titulo, autor, paginas, pagina_actual):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pagina_actual = pagina_actual
    def avanzar_pagina(self):
            if self.pagina_actual < self.paginas:
                self.pagina_actual += 1
    def retroceder_pagina(self):
            if self.pagina_actual > 1:
                        self.pagina_actual -= 1
    def ir_a_pagina(self, numero_pagina):
            if 1 <= numero_pagina <= self.paginas:
                self.pagina_actual = numero_pagina
            else:
                print("Número de página inválido.")
                 
    def consultar_pagina_actual(self):
            return self.pagina_actual
    def informacion_libro(self):
            return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}, Página Actual: {self.pagina_actual}"
titulo = input("ingrese el titulo del libro:")
autor = input("ingrese el autor del libro:")
paginas = int(input("ingrese el numero de paginas del libro: "))
pagina_actual = int(input("ingrese la pagina actual del libro: "))
libro1 = libro(titulo, autor, paginas, pagina_actual)
libro1.avanzar_pagina()
print("pagina actual despues de avanzar:", libro1.consultar_pagina_actual())

libro1.retroceder_pagina()
print("pagina actual despues de retroceder:", libro1.consultar_pagina_actual())
 
nueva_pagina = int(input("ingrese una nueva pagina para ir: "))
libro1.ir_a_pagina(nueva_pagina)

print("pagina actual despues de ir a nueva pagina: ", libro1.consultar_pagina_actual())

print("informacion del libro:", libro1.informacion_libro())
