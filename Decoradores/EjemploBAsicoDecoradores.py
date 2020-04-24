def funcionDecoradora(funcionParametro):
    
    def funcionInterior():
        print("Vamos a Realizar un calculo")
        funcionParametro()
        print("Se realizo el calculo")
    
    return funcionInterior


@funcionDecoradora
def suma():
    print(10+30)

def resta():
    print(30-15)


suma()

resta()
