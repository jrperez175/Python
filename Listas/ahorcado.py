IMAGENES=['''
 +---+
 |   |
     |
     |
     |
     |
     ========
''','''
 +---+
 |   |
 O   |
     |
     |
     |
     ========
''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
     ========
''','''
 +---+
 |   |
 O   |
/|   |
     |
     |
    ========
''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
    ========
''','''
 +---+
 |   |
 O   |
/|\  |
 |   |
     |
    ========
''','''
 +---+
 |   |
 O   |
/|\  |
 |   |
/    |
    ========
''','''
 +---+
 |   |
 O   |
/|\  |
 |   |
/ \  |
    ========
''']

PALABRAS=[
    "lavadora",
    "secadora",
    "sofa",
    "gobiernos",
    "diputado",
    "democracia",
    "computador",
    "teclado"
]

import random


def run():
    palabra = aleatoria_palabra()
    palabra_oculta = ['_'] * len(palabra)
    letras_elegidas = []
    intentos = 0

    while True:
        mostrar_tablero(palabra_oculta, intentos, letras_elegidas)
        letra_elegida = input("Escoge una letra: ")

        letras_elegidas.append(letra_elegida)

        index_letras = []

        for idx in range(len(palabra)):
            if palabra[idx] == letra_elegida:
                index_letras.append(idx)

        if len(index_letras) == 0:
            intentos += 1
            if verificarSiPerdio(intentos, palabra_oculta, palabra, letras_elegidas):
                break

        else:
            for idx in index_letras:
                palabra_oculta[idx] = letra_elegida

        index_letras = []

        if verificarSiGano(palabra_oculta, palabra):
            break


def verificarSiPerdio(intentos, palabra_oculta, palabra, letras_elegidas):
    if intentos == 7:
        mostrar_tablero(palabra_oculta, intentos, letras_elegidas)
        print(" ")
        print("¡PERDISTE!, la palabra correcta era: {}".format(palabra))
        return True


def verificarSiGano(palabra_oculta, palabra):
    if "".join(palabra_oculta) == palabra:
        print("¡GANASTE! Felicidades. La palabra es: {}".format(palabra))
        print(" ")
        return True

        '''try:
            palabra_oculta.index("_")
        except ValueError:
            print("¡GANASTE! Felicidades. La palabra es: {}".format(palabra))
            print(" ")
            break
        '''


def aleatoria_palabra():
    idx = random.randint(0, len(PALABRAS) - 1)
    return PALABRAS[idx]


def mostrar_tablero(palabra_oculta, intentos, letras_elegidas):
    print(IMAGENES[intentos])
    print("")
    print(palabra_oculta)
    print("")
    letras_elegidas.sort()
    print("Letras Elegidas: {}".format(letras_elegidas))
    print("--- * --- * --- * --- * --- * --- * --- * ")


if __name__ == "__main__":
    print("B I E N V E N I D O S A A H O R C A D O S")

    run()
