def sumarRecursivamente(numeroASumarRecursivamente):
    if numeroASumarRecursivamente <=0:
        return 0
    
    return numeroASumarRecursivamente + sumarRecursivamente(numeroASumarRecursivamente-1)

def factorialRecursivo(numeroABuscarFactorial):
    if numeroABuscarFactorial == 0:
        return 1
    
    return numeroABuscarFactorial * factorialRecursivo(numeroABuscarFactorial-1)


def potenciaRecursiva(numeroAPotenciar, potenciaDeseada):
    if potenciaDeseada == 0:
        return 1
    
    return numeroAPotenciar * potenciaRecursiva(numeroAPotenciar,potenciaDeseada-1)


if __name__ == '__main__':
    while True:
        print(''' 
        
        Opciones del Menu 
        
        S[U]ma Recursiva
        [P]otencia
        [F]actorial
        [S]alir
        ''')
        
        comando = input ('Digite la opcion deseada: ').lower()
        try:
            if comando == 'u':
                numeroASumarRecursivamente = int(input('Ingrese el Numero Entero a Sumar Recurivamente: ')) 
                resultadoSumaRecursiva = sumarRecursivamente(numeroASumarRecursivamente)
                print('La suma recursiva del numero {} es: {}'.format(numeroASumarRecursivamente,resultadoSumaRecursiva))
            elif comando == 'p':
                datosSolicitadosParaLaPotencia = input('Ingrese el Numero  y su Potencia separados por ",": ')
                listaParametros = datosSolicitadosParaLaPotencia.split(",")
                resultadoPotencia = potenciaRecursiva(int(listaParametros[0]),int(listaParametros[1]))
                print('La potencia del numero {}  a la {} es: {}'.format(listaParametros[0],listaParametros[1],resultadoPotencia))
            elif comando == 'f':
                numeroABuscarFactorial = int(input('Ingrese el Numero Entero que desee buscar su Factorial: '))
                resultadoFactorial = factorialRecursivo(numeroABuscarFactorial)
                print('El factorial del numero {} es: {}'.format(numeroABuscarFactorial,resultadoFactorial))

            elif comando == 's':
                break
        except ValueError:
            print("Ingreso Invalido, por favor digite un numero Entero positivo")
        

        
