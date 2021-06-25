class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre  # Atributos de clase
        self.apellido = apellido
        self.edad = edad
        self.sexo = 'M'  # Se pueden definir atributos fijos

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

print(type(Persona))
print(f'---------------------------------------')
print(f'Imprimiendo con un variable que contienen el objeto')
persona1 = Persona('Jhon', 'Perez', 49)  ##Llama al constructor de la clase, indirectamente es el metodo init
print(f'Mi nombre es: {persona1.nombre} , mi apellido es {persona1.apellido} , mi edad es {persona1.edad} y mi sexo es {persona1.sexo}')

persona2 = Persona('Raul', 'Muñoz', 49)  ##Llama al constructor de la clase, indirectamente es el metodo init
print(f'Mi nombre es: {persona2.nombre} , mi apellido es {persona2.apellido} , mi edad es {persona2.edad}')

#Modificar valores del objeto
print(f'---------------------------------------')
print(f'Modificando valores de los objetos')
persona1.nombre = "Jhon Raul"
persona1.apellido = 'Perez Muñoz'
print(f'Mi nombre es: {persona1.nombre} , mi apellido es {persona1.apellido} , mi edad es {persona1.edad} y mi sexo es {persona1.sexo}')


#Metodos de Instancia
print(f'---------------------------------------')
print(f'Imprimiendo con un medodo de instancia')
persona1.mostrar_detalle()
persona2.mostrar_detalle()

#Llamar un metodo directamente desde la clae
print(f'Imprimiendo utilizando la llamada del metodo directamente desde la clase')
Persona.mostrar_detalle(persona1)

#Adicionar atributos a un objeto
print(f'Adicionar atributos a un objeto')
persona1.telefono = '300XXXX' #Este atributo no se comparte con los demas objetos
print (persona1.telefono)
print (persona2.telefono)