class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre  # Atributos de clase
        self.apellido = apellido
        self.edad = edad
        self.sexo = 'M'  # Se pueden definir atributos fijos


# print(type(Persona))
persona1 = Persona('Jhon', 'Perez', 49)  ##Llama al constructor de la clase, indirectamente es el metodo init
print(f'Mi nombre es: {persona1.nombre} , mi apellido es {persona1.apellido} , mi edad es {persona1.edad} y mi sexo es {persona1.sexo}')

persona2 = Persona('Raul', 'Muñoz', 49)  ##Llama al constructor de la clase, indirectamente es el metodo init
print(f'Mi nombre es: {persona2.nombre} , mi apellido es {persona2.apellido} , mi edad es {persona2.edad}')
