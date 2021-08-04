class Persona2:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre  # Define un atribito como encapsulados y debe ser manejado dentro de la misma clase pero no es restrictivo, es decir se puedemodificar por fuera de la clase
        #self.__apellido = apellido # Define un atribito como encapsulados y debe ser manejado dentro de la misma clase pero es restrictivo, es decir no se puede modificar por fuera de la clase
        self.__apellido = apellido
        self.__edad = edad

    #Creacion de un metodo que funciona como un atributo por medio del decorado properties
    # Modifica el comportamiento del metodo, para poder accderlo como un atributo de la clase
    #Funciona como un getter
    @property
    def nombre(self):
        print('Llmando al atributo por medio del decorador property')
        return self.__nombre

    @property
    def apellido(self):
        print('Llmando al atributo por medio del decorador property')
        return self.__apellido

    @property
    def edad(self):
        print('Llmando al atributo por medio del decorador property')
        return self.__edad
    # Creacion de un metodo que funciona como un atributo por medio del decorado x.setter
    # Modifica el comportamiento del metodo, para poder accderlo como un atributo de la clase
    # Funciona como un setter
    @nombre.setter
    def nombre(self,nombre):
        print('Llamando al atributo por medio del decorador setter')
        self.__nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        print('Llamando al atributo por medio del decorador setter')
        self.__apellido = apellido

    @edad.setter
    def edad(self, edad):
        print('Llamando al atributo por medio del decorador setter')
        self.__edad = edad



    def mostrar_detalle(self):
        print(f'Persona: {self.__nombre} {self.__apellido} {self.__edad}')

persona1 = Persona2('Juan','Perez',49)

##### Encapsulamiento
#persona1._nombre = 'Raul' #Se puede asiganr nuevo valor al atributo encapsulado, es una notacion sugerida pero no es restrictiva
#persona1.__apellido = 'Acosta' # No Se puede asignar nuevo valor al atributo encapsulado, es restricitva pero poco se utiliza
#persona1.mostrar_detalle()


#### Decorador Properties
print(persona1.nombre)
persona1.mostrar_detalle()

#### Decorador setter
persona1.nombre = 'Jhon'
persona1.apellido = 'Muñoz'
persona1.edad = 50
persona1.mostrar_detalle()
