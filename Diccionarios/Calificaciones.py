MATERIAS = ("MATEMATICAS", "SISTEMAS", "QUIMICA", "ESPAÑOL")


def calcularPromedio(calificaciones):
    sumatoriaNotas = 0
    for notas in calificaciones.values():
        sumatoriaNotas += notas

    promedio = sumatoriaNotas / len(calificaciones)
    return promedio


def ingresarCalificaciones():
    print("B I E N V E N I D O S")
    print("C A L I F I C A C I O N E S")
    print("")
    calificaciones = {}

    for materia in MATERIAS:
        nota = int(input("Digite la calificacion de la materia {} : ".format(materia)))
        calificaciones[materia] = nota
    return calificaciones


if __name__ == "__main__":
    calificaciones = ingresarCalificaciones()
    resultado = calcularPromedio(calificaciones)

    print("El promedio de las notas es: {}".format(resultado))
