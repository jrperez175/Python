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
def listarNombres(*nombres): #Usualmente en la literatura se utiliza la expresion def fun(*arg):
    for nombre in nombres:
        print(nombre)

# Funciones que reciben Diccionarios (Parametros llave-valor)
def listarTerminos(**terminos): #Usualmente en la literatura se utiliza la expresion def fun(**kwarg):
    for llave , valor in terminos.items():
        print(f'la llave es: {llave} y el valor es: {valor}')

# Funciones con varios tipos de valores
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

#Funcion recursiva
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

def imprimirValoresdescendientesRecusrsivamente(numero):
    if numero != 0:
        print(numero)
        imprimirValoresdescendientesRecusrsivamente(numero - 1)


if __name__ == "__main__":
    # miFuncion() #las funciones deben ser declaradas antes de ser llamadas
    # miFuncionParametros('Jhon', 'Raul')
    # miFuncionParametros('Karla', 'Lara')
    #resultado = sumar(5, 3);
    #print(f'El resultado de la suma es: {resultado}')
    #print(f'El resultado de la suma es: {sumar(5, 5)}')
    #print(f'El resultado de la suma es: {sumarConParametrosDefault()}')
    #listarNombres('Jhon','Raul')
    #listarNombres('Jhon','Raul','Perez','Munoz')
    #listarTerminos(IDE='Integrated Developement Enviroment'
    #               ,PK='Primary Key'
    #               ,PI=3.1416) #La llave del diccionario no lleva comillas y el valor puede se cualquier dato
    #listarTerminos(DBMS='Database Management System')
    #desplegarNombres(['Jhon','Raul','Alejandro','Nicolas','Olga'])
    #desplegarNombres('Jhon')
    #desplegarNombres(10) #Genera error porque no se puede  iterar sobre un int
    #desplegarNombres(10,11) #Genera un error porque se esta definiendo que se envian 2 parametros
    #desplegarNombres((10, 11)) #Ejecuta correctamente porque se envia una tupla de dos valores
    #desplegarNombres((10,)) #Ejecuta correctamente porque se envia una tupla de un valores
    #print(f'El factorial de 5 es: {factorial(5)}')
    imprimirValoresdescendientesRecusrsivamente(5)