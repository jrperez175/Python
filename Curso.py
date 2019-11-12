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
    print(elemento)


print("Ciclo if define rama a ejecutar")
if numero1==5:
    print("Sentecia Afirmativa")
else:
    print("Sentencia Negativa")

print("Definir un metodo")
def sumar2Numeros(num1,num2):
    return (num1+num2)

print("Suma de dos numeros por un metodo: " + str(sumar2Numeros(numero1,numero2)))
