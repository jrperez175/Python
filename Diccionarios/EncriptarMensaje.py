LLAVES = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
    'á': '*',
    'é': '/',
    'í': '&',
    'ó': '$',
    'ú': '!',
    '(': '-',
    ')': '_',
}


def cifrarMensaje(mensaje):
    palabras = mensaje.split(" ")
    mensajeCifrado = []

    for palabra in palabras:
        palabraCifrada = ""

        for letra in palabra:
            palabraCifrada += LLAVES[letra]

        mensajeCifrado.append(palabraCifrada)

    return " ".join(mensajeCifrado)


def descifrarMensaje(mensaje):
    palabras = mensaje.split(" ")
    mensajeDescifrado = []

    for palabra in palabras:
        palabraDescifrada = ""

        for letra in palabra:

            for llave, valor in LLAVES.items():
                if valor == letra:
                    palabraDescifrada += llave

        mensajeDescifrado.append(palabraDescifrada)

    return " ".join(mensajeDescifrado)


def run():
    while True:
        print('''--- * --- * --- * --- * --- * --- * --- * ---

                    Bienvenido a criptografía. ¿Qué deseas hacer?

                    [c]ifrar mensaje
                    [d]ecifrar mensaje
                    [s]alir
                    
                ''')

        accion = input("Elije la opcion: ")

        if accion == "c":
            mensaje = input("Escribe tu mensaje: ")
            mensajeCifrado = cifrarMensaje(mensaje)
            print(mensajeCifrado)
        elif accion == "d":
            mensaje = input("Escribe tu mensaje Cifrado: ")
            mensajeDesencriptado = descifrarMensaje(mensaje)
            print((mensajeDesencriptado))
        elif accion == "s":
            print("Salir")
            break
        else:
            print("Comando no encontrado")


if __name__ == "__main__":
    print('M E N S A J E S  C I F R A D O S')
    run()
