numero1=1
numero2=5
msg="hola mundo"
listas_nombre=["Jhon","Raul","Perez","Muñoz"]
print("Imprime la variable msg: " + msg)
print(listas_nombre)
print("Imprimiendo un elemento de la lista: {0}".format(listas_nombre[2]))


print("Longitud de la lista: " + str(len(listas_nombre)))
print("Colocando Capitalizable el string msg: " + msg.capitalize())
print(msg.split())

print("Elementos de una Lista por medio de un bucle")
for elemento in listas_nombre:
    print("Los elementos de la lista son: {0}".format(elemento))

print("Bucle For con ragos")
x=0
for index in range(10):
    x+=10
    print("El valor de X es: {0}".format(x))
    


print("Tipo de dato range")
x=range(10)
print(list(x))
x=range(2,10)
print(list(x))
x=range(2,10,3)
print(list(x))

 
print("Ciclo if define rama a ejecutar")
if numero1==5:
    print("Sentecia Afirmativa")
else:
    print("Sentencia Negativa")

print("Definir un metodo")
def sumar2Numeros(num1,num2):
    return (num1+num2)

print("Suma de dos numeros por un metodo: " + str(sumar2Numeros(numero1,numero2)))

print("Diccionarios")

estudiante = {
    "Name":"jhon",
    "Tipo_Doc":"Cedula",
    "Num_Doc": 98536175,
    "Direccion": None
}

print("----------------------")
print("Manejo de Excepciones")
print("----------------------")
try:
    Apellido = estudiante["Apellido"]
except KeyError as error:
    print("Error buscando apellido")
    print(error)

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




numeroEstudiantes=[
    {"name":"jhon","Tipo_Doc":"Cedula","Num_Doc": 99999999,"Direccion": None},
    {"name":"raul","Tipo_Doc":"T.I","Num_Doc": 88888888,"Direccion": "Carrera 40"},
    {"name":"perez","Tipo_Doc":"NIT","Num_Doc": 7777777,"Direccion": "Carrera 48"}
]
print("Arreglo de Diccionarios")
print(numeroEstudiantes)
print(numeroEstudiantes[0].get("name"))

username = input("Ingrese su nombre:")
print(username)

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