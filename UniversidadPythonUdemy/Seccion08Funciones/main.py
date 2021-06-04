#miFuncion() #Genera un error porque primero debe ser declarada

def miFuncion():
    print("Saludos desde mi funcion")

def miFuncionParametros(nombre, apellido):
    print(f"Tu nombre y apellido es: {nombre} {apellido}")

def sumar(a, b):
    return a + b

if __name__=="__main__":
    #miFuncion() #las funciones deben ser declaradas antes de ser llamadas
    #miFuncionParametros('Jhon', 'Raul')
    #miFuncionParametros('Karla', 'Lara')
    resultado = sumar(5, 3); print(f'El resultado de la suma es: {resultado}')
    print(f'El resultado de la suma es: {sumar(5, 5)}')
