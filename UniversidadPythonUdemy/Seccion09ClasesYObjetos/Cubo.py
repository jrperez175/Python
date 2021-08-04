class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo

if __name__ == '__main__':
    ancho = int(input('Ingrese el ancho: '))
    alto = int(input('Ingrese lo alto: '))
    profundo = int(input('Ingrese lo profundo: '))

    cubo1 = Cubo(ancho, alto, profundo)
    print(f'El volumen del Cubo es: {cubo1.calcular_volumen()}')