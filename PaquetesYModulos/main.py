from Lampara import EncenderLampara

def run():
    lamp = EncenderLampara(is_turned_on = False)

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
