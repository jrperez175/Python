# miFuncion() #Genera un error porque primero debe ser declarada

def miFuncion():
    print("Saludos desde mi funcion")


def miFuncionParametros(nombre, apellido):
    print(f"Tu nombre y apellido es: {nombre} {apellido}")


# def sumar(a:int, b:int) -> int POodemos brintar informacion acerca del tipo de parametros
def sumar(a, b):
    return a + b


# Parametros por default
def sumarConParametrosDefault(a=5, b=7):
    return a + b


# Funciones sin definir numero de parametros
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

# Funciones con parametros llave-valor

if __name__ == "__main__":
    # miFuncion() #las funciones deben ser declaradas antes de ser llamadas
    # miFuncionParametros('Jhon', 'Raul')
    # miFuncionParametros('Karla', 'Lara')
    resultado = sumar(5, 3);
    print(f'El resultado de la suma es: {resultado}')
    print(f'El resultado de la suma es: {sumar(5, 5)}')
    print(f'El resultado de la suma es: {sumarConParametrosDefault()}')
    listarNombres('Jhon','Raul')
    listarNombres('Jhon','Raul','Perez','Munoz')