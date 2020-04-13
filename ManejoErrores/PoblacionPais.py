paises = {
    "colombia": 49,
    "mexico": 122,
    "argentina": 43,
    "chile": 18,
    "peru": 31
}

if __name__ == '__main__':
    while True:

        pais = input("Ingrese el Pais que desea conocer la poblacion: ").lower()

        try:
            print("La poblacion de {} es: {} millones".format(pais, paises[pais]))
        except KeyError:
            print("No se tiene el dato de la poblacion del país {}, digite de nuevo".format(pais))
        finally:
            if not input("Desea seguir consultando (S) o (N) : ").lower() == "s":
                break
