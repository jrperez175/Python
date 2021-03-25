import random


def busquedaBinaria(listaDeNumeros, numeroBuscar):
    numeroFinal = len(listaDeNumeros) - 1
    numeroEncontrado = False
    for numero in range(len(listaDeNumeros)):
        numeroInicial = numero
        numeroMitad = int((numeroInicial + numeroFinal) / 2)

        if listaDeNumeros[numeroMitad] == numeroBuscar:
            print("Se Encontro el Numero en la posicion {}: ".format(numeroMitad))
            numeroEncontrado = True
            break
        elif numeroMitad < numeroBuscar:
            numero = numeroMitad
        else:
            numeroFinal = numeroMitad

    if not numeroEncontrado:
        print("Numero no Encontrado")


def busquedaBinaria2(listaDeNumeros, numeroBuscar, indiceBajo, indiceAlto):
    if indiceBajo > indiceAlto:
        return False

    indiceMedio = int((indiceBajo + indiceAlto) / 2)

    if listaDeNumeros[indiceMedio] == numeroBuscar:
        return True
    elif listaDeNumeros[indiceMedio] > numeroBuscar:
        return busquedaBinaria2(listaDeNumeros, numeroBuscar, indiceBajo, indiceMedio - 1)
    else:
        return busquedaBinaria2(listaDeNumeros, numeroBuscar, indiceMedio + 1, indiceAlto)


def generarListasNumericaAleatoria(numeroAleatoriosAGenerar, numeroLimite):
    listaDeNumeros = []
    i = 0

    while i < numeroAleatoriosAGenerar:
        numero = random.randint(0, numeroLimite)

        try:
            listaDeNumeros.index(numero)
        except ValueError:
            listaDeNumeros.append(numero)
            i += 1

    listaDeNumeros.sort()

    return listaDeNumeros


if __name__ == "__main__":

    numeroAleatoriosAGenerar = int(input("Ingrese el numero aleatorios a generar: "))
    numeroLimite = int(input("Ingrese el el valor maximo del numero que desea generar aleatorio: "))
    listaDeNumeros = generarListasNumericaAleatoria(numeroAleatoriosAGenerar, numeroLimite)
    print(listaDeNumeros)

    numeroBuscar = int(input("Ingrese el numero que desee encontrar: "))
    indiceBajo = 0
    indiceAlto = len(listaDeNumeros) - 1
    # busquedaBinaria(listaDeNumeros,numeroBuscar)
    resultado = busquedaBinaria2(listaDeNumeros, numeroBuscar, indiceBajo, indiceAlto)
    if resultado is True:
        print("El numero {} esta en la lista".format(numeroBuscar))
    else:
        print("El numero {} no esta en la lista".format(numeroBuscar))