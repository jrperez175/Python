
def protegida(funcion):
    
    def encapsula(contraseña):
        
        if contraseña=="platzi":
            return funcion()
        else:
            print("La Contraseña Incorrecta")

    return encapsula


@protegida
def funcion_protegida():
    print("Tu contraseña es correcta.")

if __name__ == "__main__":
    contraseña = input("INgresa tu contraseña: ")
    
    funcion_protegida(contraseña)