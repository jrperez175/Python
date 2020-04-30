import csv

class Contacto:
    def __init__(self, nombre,telefono,email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self._contactos = []
    
    def adicionar(self,nombre, telefono,email):
        contacto = Contacto(nombre,telefono,email)
        self._contactos.append(contacto)
        self._guardarEnArchivo()
    
    def motrarContactos(self):

        for contacto in self._contactos:
            self._imprimirContacto(contacto)
    
    def _imprimirContacto(self,contacto):
        print('--- * --- * --- * --- * --- * --- * --- * --- * --- ')
        print('Nombre: {}'.format(contacto.nombre))
        print('Telefono: {}'.format(contacto.telefono))
        print('Email: {}'.format(contacto.email))
        print('--- * --- * --- * --- * --- * --- * --- * --- * --- ')

    def  borrarContacto(self,nombre):
        
        for idx, contacto in enumerate(self._contactos):
            if contacto.nombre.lower() == nombre.lower():
                del self._contactos[idx]
                self._guardarEnArchivo()
                print('Se encontro el contacto {} y se procedio son su borrrado'.format(nombre))
                break
        
        else:
            self._noEncontrado()

    def _guardarEnArchivo(self):
        with open('agenda.csv','w',newline='',encoding='utf-8') as f:
            escribir = csv.writer(f)
            escribir.writerow(('nombre','telefono','email'))

            for contacto in self._contactos:
                escribir.writerow((contacto.nombre,contacto.telefono,contacto.email))

        
    def buscarContacto(self,nombre):
         for contacto in self._contactos:
             if contacto.nombre.lower() == nombre.lower():
                 self._imprimirContacto(nombre)
                 break
         else:
            self._noEncontrado()
    
    def _noEncontrado(self):
        print('*************************')
        print('¡ No Se Encontrado el Contacto !')
        print('*************************')

    def modificarContacto(self,nombre):
        for contacto in (self._contactos):
             if contacto.nombre.lower() == nombre.lower():

                 print('¡ Dejar en blanco si no se desea modificar algun dato !')

                 nombre = input('Digita el nuevo nombre: ')
                 telefono = input('Digita el nuevo numero telefonico: ')
                 email = input('Digita el nuevo email: ')
                 
                 if  nombre != '':
                     contacto.nombre = nombre
                 
                 if telefono != '':                    
                     contacto.telefono = telefono
                 
                 if email != '':
                     contacto.email =email
                 break
        
        else:
            self._noEncontrado()


def run():

    agenda = Agenda()

    try:
        
        with open('agenda.csv','r',encoding='utf-8') as f:
            leer = csv.reader(f)

            for idx, fila in enumerate(leer):
                if idx == 0:
                    continue

                agenda.adicionar(fila[0],fila[1],fila[2])
    
    except FileNotFoundError:
        with open ('agenda.csv','w',encoding='utf-8'):
            print('Archivo agenda.csv no encontrado, se procedio a crearlo')
            
    while True:
        print(''' 
        
        Opciones del Menu 
        
        [a]ñadir contacto
        ac[t]ualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contacto
        [s]alir 
        ''')
        
        comando = input ('Digite la opcion deseada: ')

        if comando == 'a':
            nombre = input('Digita el nombre: ')
            telefono = input('Digita el numero telefonico: ')
            email = input('Digita el email: ')

            agenda.adicionar(nombre,telefono,email)
            
        elif comando == 't':
           nombre = input('Digita el nombre a Modificar: ') 
           agenda.modificarContacto(nombre)
        elif comando == 'b':
           nombre = input('Digita el nombre a Buscar: ')
           agenda.buscarContacto(nombre)
        elif comando == 'e':
            nombre = input('Digita el nombre a Eliminar: ')
            agenda.borrarContacto(nombre)
        elif comando == 'l':
            agenda.motrarContactos()
        elif comando == 's':
            break
        else:
            print('Comando no encontrado')

if __name__ == '__main__':
    print('B I E N V E N I D O S  A  M I  A G E N D A')
    run()
