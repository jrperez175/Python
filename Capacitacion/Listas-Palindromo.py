def palindromo():
    palabra = input("Digite la palabra: ")
    
    #palabraReves=construirPalabraReves(palabra)
    palabraReves=construirPalabraReves2(palabra)
    
    validarPalindromo(palabra,palabraReves)
    

def validarPalindromo(palabra,palabraReves):
    if(palabraReves==palabra):
        print("La palabra {} es palindromo".format(palabra))
    else:
        print("La palabra {} no es palindromo {}".format(palabra,palabraReves))


        
def construirPalabraReves2(palabra):
    palabra_reves=palabra[::-1]
    return palabra_reves


def construirPalabraReves(palabra):
    
    letras_reves = []
    
    for letras in palabra:
        letras_reves.insert(0,letras)
    
    palabra_reves = "".join(letras_reves)
    
    return palabra_reves
    
    
    

if __name__ == "__main__":
    palindromo()