class cuentahorro:
    def __init__(self, cuenta_bancaria, interes_anual):
        self.cuenta_bancaria = cuenta_bancaria
        self.interes_anual = interes_anual
        self.saldo = 0

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Saldo insuficiente.")

    def calcular_interes(self):
        return self.saldo * self.interes_anual

print("ingresa el numero de cuenta bancaria: ")
cuenta_bancaria = input()
print("ingresa el interes anual: ")
interes_anual = float(input())

cuenta1 = cuentahorro(cuenta_bancaria, interes_anual)
print("ingresa el monto a depositar: ")
monto = float(input())
cuenta1.depositar(monto)
print("saldo actual: ", cuenta1.saldo)
print("ingresa el monto a retirar: ")
monto = float(input())
cuenta1.retirar(monto)
print("saldo actual: ", cuenta1.saldo)
print("interes generado: ", cuenta1.calcular_interes())
print("saldo final: ", cuenta1.saldo + cuenta1.calcular_interes())
