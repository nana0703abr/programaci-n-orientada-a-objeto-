class tarjetacredito:
    def __init__(self, numero):
     self.numero = numero
    @staticmethod
    def validar_numero(numero):
        numero = str(numero)
        suma = 0
        invertir = numero[::-1]
        for i, digito in enumerate(invertir):
            n = int(digito)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            suma += n   
            return suma % 10 == 0
    
numero = input("ingrese el numero de la tarjeta de credito:")
if tarjetacredito.validar_numero(numero):
    print("El numero de la tarjeta de credito es valido.")
else:
    print("El numero de la tarjeta de credito no es valido.")
