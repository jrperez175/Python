#Porque aprender Python

#Instalacion

#Conocer un poco Visual Studio Code
#Ejecutar Triangulo o consola
#Debugger
#Python Interactive # %%

# %%
#Mi primer programa #Hola Mundo

mensaje = 'Hola Mundo'
print(mensaje)
print("Imprime la variable msg: " + mensaje)
print("El mensaje {} es: ".format(mensaje))

# %%
#Operadores - Evaluacion (PEMDAS)
print(3*2)
print(3/2)

# %%
#Variables - ConvencionNombrado - TiposDatos - Casting - Varible con Operadores
numEntero = 1
numFloat = 2.6
varTexto = '5'
castingvarTextoANumero = int(varTexto)
varBooleana = True

print(numEntero)
print(numFloat)
print(varTexto)
print(castingvarTextoANumero)
print(type(castingvarTextoANumero))
print(varBooleana)

print(5==3)
print(varTexto*3)

# %%
#Manejo Tipo String - Slicing - Listas - Tuplas - Diccionarios
var1 ="Hola"
var2 = 'Hola'
print(var1 == var2)
print("---------------")

#String como arreglos
mensaje = "Hello, World!"
print(mensaje[1])
print("---------------")

#Slicing
print("Slicing")
print(mensaje[2:5])
print(mensaje[:5])
print(mensaje[3:])
print(mensaje[0:8:2])
print(mensaje[::-1])
print(len(mensaje))
print(mensaje.split(","))
print("---------------")

#Listas
print("Listas")
listaVacia=[]
listas_nombre=["Jhon","Raul","Perez","Muñoz"]
listas_nombre2=["Perez","Raul","Jhon","Muñoz"]
print('Concepto de Ordenadas')
print(listas_nombre==listas_nombre2)
print(listas_nombre)
print("Imprimiendo un elemento de la lista: {0}".format(listas_nombre[2]))
print("Longitud de la lista: " + str(len(listas_nombre)))
listas_nombre.append("Durango")
listas_nombre.insert(0,"Durango")
print("---------------")

#Realizar el ejercicio Palindromo

#Tuplas
print("Tuplas")
my_tupla=(1,2,3,4)
print(my_tupla[3])
myTupla2=(1,)
print(myTupla2)
print(type(myTupla2))
print("---------------")

#Dicicionarios
print("Diccionarios")

estudiante = {
    "Name":"jhon",
    "Tipo_Doc":"Cedula",
    "Num_Doc": 98536175,
    "Direccion": None
}
print("----------------------")
print("Imprimir diccionario")
print("----------------------")

print(estudiante)

print("Nombre Antes")
print(estudiante.get("Name"))
print("Nombre Despues")
estudiante.update({"Name":"raul"})
print(estudiante["Name"])

print("Agregar otro valor al diccionario")
estudiante["Apellido"]="perez"
print(estudiante["Apellido"])

print(estudiante.keys())
print(estudiante.values())
print("---------------")

#Conjuntos
print("Conjuntos")
s = set([1,2,3])
s1 = {3,2,1}
print(s==s1)
t = set([3,4,5])
licores = ['vino', 'cerveza', 'ron', 'aguardiente', 'ron']

#Operaciones con sets
print(s.union(t)) # set([1,2,3,4,5])

print(s.intersection(t)) # set([3])

print(s.difference(t)) # set([1,2])

print(set(licores))
print("---------------")

# %%
#Estructura de Desicion IF -Operadores Relacionales (==,!=,>,<,>=,<=)- Operadores Logicos(and, or, not)
print("Ciclo if define rama a ejecutar")
numero = 3
if numero == 5:
    print("Sentecia Afirmativa")
else:
    print("Sentencia Negativa")
#Mostrar error de identacion
if numero == 5:
print("Sentecia Afirmativa")
else:
print("Sentencia Negativa")


# %%
#Estructura Condicional FOR - While
print("Elementos de una Lista por medio de un bucle")
listas_nombre=["Jhon","Raul","Perez","Muñoz"]
capitales = {'Chile':'Santiago',
              'España':'Madrid',
              'Francia':'París'}
for elemento in listas_nombre:
    print("Los elementos de la lista son: {0}".format(elemento))

print('Las claves del diccionario capitales son')
for pais in capitales.keys():  # recorre diccionario
    print(pais)

print('Los valores del diccionario capitales son')
for capital in capitales.values():  # recorre diccionario
    print(capital)

for pais, capital in capitales.items():  # recorre diccionario
    print('Capital de {0}: {1}'.format(pais, capital))



print("Tipo de dato range")
x=range(10)
#print(x)
print(list(x))
x=range(2,10)
print(list(x))
x=range(2,10,3)
print(list(x))

#For con range
print("Bucle For con rangos")
x=0
for index in range(10):
    x+=10
    print("El valor de X es: {0}".format(x))
    

#While
print("Bucle While con rangos")
i=10
while i > 0:
    print(i)
    i-=1

#Ejercicio de tablas de multiplicar
#Ejercicio PromedioTemperatura

# %%
#Funciones
print("Definir un metodo")
num1 = 4
num2 = 6
def sumar2Numeros(num1,num2):
    return (num1+num2)

print("Suma de dos numeros por un metodo: " + str(sumar2Numeros(num1,num2)))

#Manejo de argumentos variables
def var_args(name, *args):
    print(name)
    print(args)

var_args("Jhon","Perez",985361, None,True,False)

#Manejo de argumentos variables pero con identificacion
def var_args_def(name, **kwargs):
    print(name)
    print(kwargs["Apellido"],kwargs["Identificacion"],kwargs["Feedback"],kwargs["Suscripcion"])

var_args_def("Jhon",Apellido="Perez",Identificacion=985361, Feedback=None,Suscripcion=True)


# %%
#Clases
print('Definicion')
class MyClass:
  x = 5
print(MyClass)

print('Crear un objeto')
p1 = MyClass()
print(p1.x)

print('La Funcion __init__() Constructor')
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print(Definiendo Metodos)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# %%
#Excepciones

print("----------------------")
print("Manejo de Excepciones")
print("----------------------")

estudiante = {
    'Nombres':'Jhon Raul',
    'Apellidos':'Perez Muñoz',
    'Nacionalidad':'Colombiana'
}
try:
    Apellido = estudiante["Nacionalidad"]
    print(Apellido)
except KeyError as error:
    print("Error buscando nacionalidad")
    print(error)



# %%
#Peticion de informacion Por Teclado
username = input("Ingrese su nombre:")
print(username)

