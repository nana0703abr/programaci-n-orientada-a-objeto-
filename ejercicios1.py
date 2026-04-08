class producto:
    def __init__ (self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def validar_precio(self):
        if self.precio < 0:
            print("el precio no puede ser menor a 0")
        else:
            print("el precio es valido")
    
    def mostrar_precio_actual(self):
        print("el precio de:", self.nombre, "es: ", self.precio)
        
    def aplicar_descuento(self, porcentaje_descuento):
        descuento = self.precio * (porcentaje_descuento / 100)
        self.precio -= descuento
        print("el precio con descuento aplicado es: ", self.precio)
producto1 = producto(input("ingrese el nombre del producto:"), float(input("ingrese el precio del producto: ")))
descuento1 = float(input("ingrese el porcentaje de descuento:"))
producto1.aplicar_descuento(descuento1)
print("el nombre del producto es:", producto1.nombre)
print("el precio del producto es:", producto1.precio)
print("el precio del producto con el descuento aplicado es: ", producto1.precio)
cambio_precio = float(input("ingrese el nuevo precio del producto:" ))
producto1.cambiar_precio(cambio_precio)
print(" el nuevo precio del pproducto es: ", producto1.precio)
producto1.validar_precio()
producto1.mostrar_precio_actual()
