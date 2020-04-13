def convertirStringALista(secuenciaDeCaracteres):
    listaDeCaracteres = []
    for letra in secuenciaDeCaracteres[::1]:
        listaDeCaracteres.append(letra)
    return listaDeCaracteres


def numeroDeRepeticionesDeLasLetras(listaDeCaracteres):
    numeroDeRepeticionesLetra = {}
    for letra in listaDeCaracteres:
        if letra in numeroDeRepeticionesLetra:
            continue

        repeticionesPorLetra = 0
        for index in range(len(listaDeCaracteres)):
            if listaDeCaracteres[index] == letra:
                repeticionesPorLetra += 1
        numeroDeRepeticionesLetra[letra] = repeticionesPorLetra

    return numeroDeRepeticionesLetra


def primeraLetraEnNoRepetirse(cantidadDeCarateresPorLetra):

    for llave,valor in cantidadDeCarateresPorLetra.items():
        if valor==1:
            return llave
    return "-"




if __name__ == "__main__":
    secuenciaDeCaracteres = input("Digite la secuencia de caracteres: ")
    listaDeCaracteres = convertirStringALista(secuenciaDeCaracteres)
    numeroDeRepeticionesDeLasLetras(listaDeCaracteres)
    resultado = primeraLetraEnNoRepetirse(numeroDeRepeticionesDeLasLetras(listaDeCaracteres))

    if resultado != "-":
        print("La primera letra en no repetirse es: {}".format(resultado))
    else:
        print("No hay ninguna letra que no se repita")

