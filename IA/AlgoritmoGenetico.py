import random #Numeros aleatorios

modelo = [1,1,1,1,1,1,1,1,1,1] #Modelo esperado, deseamos que todos los numeros sean 1

largo = 10 #Logintud del material genetico de cada individuo
num = 10 # Poblacion
pressure = 3 #Numeros de individuos que se seleccionan para la reproduccion. Tiene que se mayor que 2 dado que uno solo no puede combinar su propio codigo genetico
mutation_chance = 0.2 # 1 Siempre muta, 0.2 es el 20 % de probabilidades que haya una mutacion

print('\n\Modelo: %s\n'%(modelo)) #Muestra el modelo que deseo llegar con un formato definido

#Crea aleatoriamente las caracteristicas (ADN) de cada individuo
def individual(min,max): 
    return [random.randint(min,max) for i in range(largo)] #Genera el codigo genetico de cada persona.

#Genera la poblacion deseada (num)
def crearPoblacion(): #La poblacion va generandose a partir de los cruces o mutaciones de los individuos
    return [individual(1,9) for i in range(num)]

#Compara cada caracteristica del individuo con su contraparte del modelo y cuenta las coincidencias

def calcularFitness(individual): #Calcula los individuos que son aptos
    fitness = 0 #Inicio sin individuos aptos
    for i in range(len(individual)): #Comienza a iteractuar con los individuos de la poblacion
        if individual[i] == modelo[i]: #Pregunta si el individuo es igual al modelo objetivo
            fitness+=1
    return fitness
        
    
def selection_and_reproduccion(population):
    #lista de tuplas (fitness, individuo)  de todos los individuos
    puntuados = [(calcularFitness(i), i) for i in population] #Cuales son los aptos o no para cada ciudadano
    puntuados = [i[1] for i in sorted(puntuados)] #Ordena por pares y se queda con los aptos
    population = puntuados #Selecciona
    
    #seleccion de individuos con mejor puntuacion (cantidad = pressure)
    selected = puntuados[(len(puntuados)-pressure):]
    
    #reproduccion: Por cada elemento restante (poblacion - selected) sucede:
    #1. se seleccionan dos individuos aleatorios entre los seleccionados
    #2. se escoge un numero aleatorio (punto) de caracteristicas del primer individuo (principio)
    #3. se toman las caracteristicas restantes del segundo individuo (final)
    #4. se reemplaza un elemento de la poblacion.
    
    for i in range(len(population)-pressure):
        punto = random.randint(1, largo-1) #Se elige el punto del codigo genetico de intercambio
        padre = random.sample(selected,2)
        population[i] [:punto] = padre[0][:punto] #Se mezcla el materia genetico
        population[i][punto:] = padre[1][punto:]
    return population

#Mutacion de los individuos de forma aleatoria
def mutacion(population):
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance: #Posibilidad de mutacion
            punto = random.randint(0,largo-1) #Elije un punto al azar para mutar
            nuevo_valor = random.randint(1,9) #Nuevo valor de punto
            
            while nuevo_valor == population[i][punto]: #Itera si el valor de punto antes es igual al nuevo (para que sean diferentes)
                nuevo_valor = random.randint(1,9) #
            
            population[i][punto] = nuevo_valor
    return population

def main():
    population = crearPoblacion()
    print('Poblacion Inicial:\n%s'%(population))

    for i in range(100):
        population = selection_and_reproduccion(population)
        population = mutacion(population)

    print('\nPoblacion Final:\n%s'%(population))
    print('\n\n')
    

if __name__ == '__main__':
    main()
    