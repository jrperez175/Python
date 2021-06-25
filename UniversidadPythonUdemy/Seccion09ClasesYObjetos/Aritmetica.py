class Aritmetica:
    """
    Clase Aritmetica par realizar las operaciones de sumar , restar, etc
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        try:
            # return round(self.operandoA / self.operandoB,3)
            return int(((self.operandoA / self.operandoB) * (10**2))) / (10**2)
        except ZeroDivisionError:
            return "Error , no se puede dividir por 0"

aritmetica1 = Aritmetica(5,3)
print(f'El resultado de la suma es: {aritmetica1.sumar()}')
print(f'El resultado de la resta es: {aritmetica1.restar()}')
print(f'El resultado de la multiplicacion es: {aritmetica1.multiplicar()}')
print(f'El resultado de la division es: {aritmetica1.dividir()}')