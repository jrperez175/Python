def run():
    while True:
        print('''--- * --- * --- * --- * --- * --- * --- * ---

                    Bienvenido a Evaluar Pequeño Teorema FERMAT. ¿Qué deseas hacer?

                    [e]valuar Teorema
                    [s]alir
                    
                ''')

        accion = input("Elije la opcion: ")

        if accion == "e":
            numero1 = int(input("Escribe el primer numero (a): "))
            numero2 = int(input("Escribe tu primer numero (p): "))
            resultado = teorema_fermat(numero1,numero2)
            if resultado == 0:
                print('La Expresion (a^p - a) es divisible por {}'.format(numero2))
            else:
                print('La Expresion (a^p - a) no divisble por {}'.format(numero2))
    
        elif accion == "s":
            print("Salir")
            break
        else:
            print("Comando no encontrado")

def teorema_fermat(numero1,numero2):
    return (((numero1 ** numero2)-numero1) % numero2)
    
    
            
            
if __name__ == '__main__':  
    run()
    