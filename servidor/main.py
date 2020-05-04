from flask import Flask, render_template, request
from modelo_contacto import Contacto

app = Flask(__name__)

@app.route(r'/', methods=['GET'])
def agenda():
    #return "Hola Ingenieros de Softaware de Platzi"
    return render_template('agenda.html')

@app.route(r'/adicionar', methods=['GET', 'POST'])
def adicionarContacto():

    if request.form:
        contacto = Contacto(nombre=request.form.get('nombre'),
                            telefono=request.form.get('telefono'),
                            email=request.form.get('email'))
        contacto.put()

        print(request.form.get('nombre'))
        print(request.form.get('telefono'))
        print(request.form.get('email'))

    return render_template('adicionar_contacto.html')

if __name__ == "__main__":
    app.run()
