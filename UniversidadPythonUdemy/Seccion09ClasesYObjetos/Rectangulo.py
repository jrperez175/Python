class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

if __name__ == "__main__":
    base = int(input('Proporcione la base del rectangulo: '))
    altura = int(input('Proporcione la altura del rectangulo: '))
    areaRectangulo1 = Rectangulo(base,altura)
    print(f'El área del rectangulo1 es igual a: {areaRectangulo1.calcular_area()}')
