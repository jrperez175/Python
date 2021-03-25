
class Lampara:

    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self,is_turned_on):
        self._is_turned_on = is_turned_on
    
    def turn_on(self):
        self._is_turned_on = True
        self._display_imagen()


    def turn_off(self):
        self._is_turned_on = False
        self._display_imagen()

    def _display_imagen(self):
        if self._is_turned_on :
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
    
def run():
    lamp = Lampara(is_turned_on = False)

    while True:
        print('''
        Que deseas hacer?

        [e] : Encender
        [a] : Apagar
        [s] : Salir
        
        ''')
        command = input("Digita tu opcion: ").lower()

        if command == "e":
            lamp.turn_on()
        elif command == "a":
            lamp.turn_off()
        else:
            break




if __name__ == "__main__":
    run()
